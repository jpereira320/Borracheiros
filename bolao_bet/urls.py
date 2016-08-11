from django.conf.urls import url
from F1Bet import views


app_name = 'bolao_bet'

urlpatterns = [
    # /F1Bet/
    url(r'bet/add/$', views.BetCreate.as_view(), name='f1bet-add'),
    # make post
    url(r'^make_post/(?P<bet_id>[0-9]+)/$', views.make_post, name='make-post'),
]

