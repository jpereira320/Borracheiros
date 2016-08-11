from django.conf.urls import url
from bolao_main import views

app_name = 'bolao_main'

urlpatterns = [
    # /F1main/
    url(r'^$', views.index, name='index'),
]
