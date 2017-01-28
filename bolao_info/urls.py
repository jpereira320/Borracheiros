from django.conf.urls import url
from bolao_info import views


app_name = 'bolao_info'

urlpatterns = [
    url(r'^select_gp/$', views.select_gp_2_update, name='info-selectgp'),
    url(r'^update_gp/$', views.update_gp, name='info-updategp'),
]
