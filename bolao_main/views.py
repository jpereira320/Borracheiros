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
from bolao_main.forms import UserDetailsForm
from bolao_bet.models import UserGpPoints, UserTotalPoints
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def next_gp():
    if GPInfo.objects.filter(race_date__gte=timezone.now()).exists():
        next_gp = GPInfo.objects.filter(race_date__gte=timezone.now()).earliest('race_date')
    else:
        next_gp = None
    
    return next_gp


def last_processed_gp():
    if GPInfo.objects.filter(processed=True).exists():
        last_processed_gp = GPInfo.objects.filter(processed=True).latest('race_date')
    else:
        last_processed_gp = None
    
    return last_processed_gp


def last_gp_results(gp):
    if UserGpPoints.objects.filter(GPrix=gp).exists():
        qs = UserGpPoints.objects.filter(GPrix=gp).order_by('-points', 'user__first_name')
        
        list_user = []
        list_points = []

        # import pdb;
        # pdb.set_trace()
        
        for item in range(0, qs.count()):
            list_user.append(qs[item].user.first_name)
            list_points.append(qs[item].points)
            
    else:
        list_user = list_points = None
    
    return list_user, list_points


def ranking(gp):
    if UserTotalPoints.objects.filter(GPrix=gp).exists():
        qs = UserTotalPoints.objects.filter(GPrix=gp).order_by('-points', 'user__first_name')
        
        list_user = []
        list_points = []
        
        for item in range(0, qs.count()):
            list_user.append(qs[item].user.first_name)
            list_points.append(qs[item].points)
            
    else:
        list_user = list_points = None
    
    return list_user, list_points


def latest_posts():
    n_posts = 35
    return Blog.objects.all()[max(Blog.objects.all().__len__() - n_posts, 0):Blog.objects.all().__len__():-1]


def index(request):
    last_gp = last_processed_gp()
    list_user, list_points = last_gp_results(last_gp)
    ranking_list_user, ranking_list_points = ranking(last_gp)
    
    # import pdb;
    # pdb.set_trace()
    
    return render(request, 'bolao_main/index.html', {
        'posts': latest_posts(),
        'next_race': next_gp(),
        'last_race': last_gp,
        'last_gp_results_user': list_user,
        'last_gp_results_points': list_points,
        'ranking_list_user': ranking_list_user,
        'ranking_list_points': ranking_list_points,
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
    return HttpResponseRedirect(reverse('bolao_main:index'))


def logout_view(request):
    logout(request)
    
    # Return to main page
    return HttpResponseRedirect(reverse('bolao_main:index'))


@staff_member_required
def change_user_password_view(request):
    username = request.POST.get('CUP_User', '')
    password = request.POST.get('CUP_Password', '')
    
    u = User.objects.get(username=username)
    u.set_password(password)
    u.save()
    
    messages.warning(request, 'Senha de ' + username + ' alterada para ' + password)
    
    # Return to main page
    return HttpResponseRedirect(reverse('bolao_main:index'))


@login_required
def change_password(request):
    if request.method == 'POST':
        
        form = PasswordChangeForm(request.user, data=request.POST)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # dont logout the user.
            messages.success(request, "Password changed.")
            
            # Return to main page
            return HttpResponseRedirect(reverse('bolao_main:index'))
    else:
        form = PasswordChangeForm(request.user)
    data = {
        'form': form
    }
    return render(request, "bolao_main/change_password.html", data)


@login_required
def user_detail_view(request):
    if request.method == 'POST':
        
        form = UserDetailsForm(request.POST)
        
        if form.is_valid():
            
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            
            if form.has_changed():
                u = User.objects.get(username=request.user.username)
                
                if request.user.first_name != first_name:
                    u.first_name = first_name
                    u.save()
                
                if request.user.last_name != last_name:
                    u.last_name = last_name
                    u.save()
        
        return HttpResponseRedirect(reverse('bolao_main:index'))
    
    else:
        
        form = UserDetailsForm(initial={'first_name': request.user.first_name, 'last_name': request.user.last_name})
    
    context = {'form': form}
    
    return render(request, 'bolao_main/user_details.html', context)
