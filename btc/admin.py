from django.contrib import admin
from btc.models import *

# Register your models here.

class UserprofileAdmin(admin.ModelAdmin):
	list_display = ('user','rate','amount','okCoin2BTCE','BTCE2okCoin','okCoin2bitfinex','bitfinex2okCoin',\
		'okcoin_key','okcoin_secret','bitfinex_key','bitfinex_secret','btce_key','btce_secret','created')
		
		
admin.site.register(Userprofile,UserprofileAdmin)