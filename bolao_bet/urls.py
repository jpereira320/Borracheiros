from django.conf.urls import url
from bolao_bet import views

app_name = 'bolao_bet'

urlpatterns = [
    # /bolao_bet/
    url(r'bet/add/$', views.BetCreate.as_view(), name='bolao_bet-add'),
    url(r'process_bet$', views.process_bet, name='bolao_bet-process'),
    url(r'view_bet$', views.view_bet, name='bolao_bet-view'),
    # make post
    url(r'^make_post/(?P<bet_id>[0-9]+)/$', views.make_post, name='make-post'),
]
