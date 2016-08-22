from django.contrib import admin
from .models import UserBet, UserGpPoints, UserTotalPoints


admin.site.register(UserBet)
admin.site.register(UserGpPoints)
admin.site.register(UserTotalPoints)