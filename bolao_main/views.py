from django.shortcuts import render
from bolao_main.models import Blog
from bolao_info.models import GPInfo
from datetime import datetime


def index(request):

    return render(request, 'bolao_main/index.html', {'posts': Blog.objects.all()[max(Blog.objects.all().__len__() - 15, 0):Blog.objects.all().__len__():-1],
                                                 'next_race': GPInfo.objects.filter(race_date__gte=datetime.now())[0]}
 )


