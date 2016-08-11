from django.conf.urls import url


app_name = 'bolao_main'

urlpatterns = [
    # /F1main/
    url(r'^$', views.index, name='index'),
]
