from django.shortcuts import render
from django.http import HttpResponseRedirect
from bolao_main.models import Blog
from bolao_info.models import GPInfo
from django.utils import timezone
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


def next_gp():
    if len(GPInfo.objects.filter(race_date__gte=timezone.now())) > 0.5:
        next_gp = GPInfo.objects.filter(race_date__gte=timezone.now()).order_by('race_date')[0]
    else:
        next_gp = None
        
    return next_gp


def latest_posts():
    n_posts = 15
    return Blog.objects.all()[max(Blog.objects.all().__len__() - n_posts, 0):Blog.objects.all().__len__():-1]


def index(request):
    
    return render(request, 'bolao_main/index.html', {
        'posts': latest_posts(),
        'next_race': next_gp(),
    })


def login_view(request):
    
    logout(request)
    
    username = request.POST.get('Username', '')
    password = request.POST.get('Password', '')
    user = authenticate(username=username, password=password)
    
    # Check for authentication and login
    if user is not None:
        # pass
        login(request, user)
    
    else:  # Authentication failed
        
        messages.warning(request, 'Login falhou! Verifique o nome de usuário e a senha')
    
    # Return to main page
    return HttpResponseRedirect(reverse('bolao_main:index'), {
        'posts': latest_posts(),
        'next_race': next_gp(),
    })


def logout_view(request):
    
    logout(request)
        
    # Return to main page
    return HttpResponseRedirect(reverse('bolao_main:index'), {
        'posts': latest_posts(),
        'next_race': next_gp(),
    })


def change_user_password_view(request):
    
    username = request.POST.get('CUP_User', '')
    password = request.POST.get('CUP_Password', '')

    u = User.objects.get(username=username)
    u.set_password(password)
    u.save()

    messages.warning(request, 'Senha de ' + username + ' alterada para ' + password)
    
    # Return to main page
    return HttpResponseRedirect(reverse('bolao_main:index'), {
        'posts': latest_posts(),
        'next_race': next_gp(),
    })


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) # dont logout the user.
            messages.success(request, "Password changed.")
            
            # Return to main page
            return HttpResponseRedirect(reverse('bolao_main:index'), {
                'posts': latest_posts(),
                'next_race': next_gp(),
            })
    else:
        form = PasswordChangeForm(request.user)
    data = {
        'form': form
    }
    return render(request, "bolao_main/change_password.html", data)
