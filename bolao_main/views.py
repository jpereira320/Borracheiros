from django.shortcuts import render
from django.http import HttpResponseRedirect
from bolao_main.models import Blog
from bolao_info.models import GPInfo
from django.utils import timezone
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.urls import reverse


def index(request):
    if len(GPInfo.objects.filter(race_date__gte=timezone.now())) > 0.5:
        next_race = GPInfo.objects.filter(race_date__gte=timezone.now()).order_by('race_date')[0]
    else:
        next_race = None
    
    return render(request, 'bolao_main/index.html', {
        'posts': Blog.objects.all()[max(Blog.objects.all().__len__() - 15, 0):Blog.objects.all().__len__():-1],
        'next_race': next_race,
    }
    )


def login_view(request):
    if len(GPInfo.objects.filter(race_date__gte=timezone.now())) > 0.5:
        next_race = GPInfo.objects.filter(race_date__gte=timezone.now()).order_by('race_date')[0]
    else:
        next_race = None
    
    logout(request)
    
    username = request.POST.get('Username', '')
    password = request.POST.get('Password', '')
    user = authenticate(username=username, password=password)
    
    # Check for authentication and login
    if user is not None:
        # pass
        login(request, user)
    
    else:  # Authentication failed
        
        messages.warning(request, 'Login falhou!')
    
    # Return to main page
    return HttpResponseRedirect(reverse('bolao_main:index'), {
        'posts': Blog.objects.all()[max(Blog.objects.all().__len__() - 15, 0):Blog.objects.all().__len__():-1],
        'next_race': next_race,
    })


def logout_view(request):
    logout(request)
    
    if len(GPInfo.objects.filter(race_date__gte=timezone.now())) > 0.5:
        next_race = GPInfo.objects.filter(race_date__gte=timezone.now()).order_by('race_date')[0]
    else:
        next_race = None
        
    # Return to main page
    return HttpResponseRedirect(reverse('bolao_main:index'), {
        'posts': Blog.objects.all()[max(Blog.objects.all().__len__() - 15, 0):Blog.objects.all().__len__():-1],
        'next_race': next_race,
    })
