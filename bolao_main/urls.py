from django.conf.urls import url
from bolao_main import views

app_name = 'bolao_main'

urlpatterns = [
    # /bolao_main/
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='main-login'),
    url(r'^logout/$', views.logout_view, name='main-logout'),
]
