from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Userprofile(models.Model):
	user = models.OneToOneField(User)
	rate = models.FloatField(default=1.0)
	amount = models.FloatField(default=1.0)
	ltcamount = models.FloatField(default=1.0)

	okCoin2BTCE = models.FloatField(default=1.0)
	BTCE2okCoin = models.FloatField(default=1.0)
	okCoin2bitfinex = models.FloatField(default=1.0)
	bitfinex2okCoin = models.FloatField(default=1.0)
	btce2bitfinex = models.FloatField(default=1.0)
	bitfinex2btce = models.FloatField(default=1.0)
	
	okCoin2huobi = models.FloatField(default=1.0)
	huobi2okCoin = models.FloatField(default=1.0)
	okCoin2btcchina = models.FloatField(default=1.0)
	btcchina2okCoin = models.FloatField(default=1.0)
	huobi2btcchina = models.FloatField(default=1.0)
	btcchina2huobi = models.FloatField(default=1.0)
	huobi2bitfinex = models.FloatField(default=1.0)
	bitfinex2huobi = models.FloatField(default=1.0)
	bitfinex2btcchina = models.FloatField(default=1.0)
	btcchina2bitfinex = models.FloatField(default=1.0)
	################
	okCoin2BTCE_ltc = models.FloatField(default=1.0)
	BTCE2okCoin_ltc = models.FloatField(default=1.0)
	okCoin2bitfinex_ltc = models.FloatField(default=1.0)
	bitfinex2okCoin_ltc = models.FloatField(default=1.0)
	btce2bitfinex_ltc = models.FloatField(default=1.0)
	bitfinex2btce_ltc = models.FloatField(default=1.0)
	
	okCoin2huobi_ltc = models.FloatField(default=1.0)
	huobi2okCoin_ltc = models.FloatField(default=1.0)
	okCoin2btcchina_ltc = models.FloatField(default=1.0)
	btcchina2okCoin_ltc = models.FloatField(default=1.0)
	huobi2btcchina_ltc = models.FloatField(default=1.0)
	btcchina2huobi_ltc = models.FloatField(default=1.0)
	huobi2bitfinex_ltc = models.FloatField(default=1.0)
	bitfinex2huobi_ltc = models.FloatField(default=1.0)
	bitfinex2btcchina_ltc = models.FloatField(default=1.0)
	btcchina2bitfinex_ltc = models.FloatField(default=1.0)

	
	okcoin_key = models.CharField(max_length=65, default="")
	okcoin_secret = models.CharField(max_length=65,default="")
	bitfinex_key = models.CharField(max_length=65,default="")
	bitfinex_secret = models.CharField(max_length=65,default="")
	btce_key = models.CharField(max_length=65,default="")
	btce_secret = models.CharField(max_length=65,default="")
	huobi_key = models.CharField(max_length=65,default="")
	huobi_secret = models.CharField(max_length=65, default="")
	btcchina_key = models.CharField(max_length=65, default="")
	btcchina_secret = models.CharField(max_length=65, default="")
	
	auto_trade = models.IntegerField(default=0)

	created = models.DateTimeField(blank=True,default=datetime.datetime.now())


class Pricebuysell(models.Model):
	okcoin_buyprice = models.FloatField()
	# btce_buyprice = models.FloatField()
	bitfinex_buyprice = models.FloatField()
	btcchina_buyprice = models.FloatField(default=0.0)
	huobi_buyprice = models.FloatField(default=0.0)

	okcoin_buyprice_ltc = models.FloatField(default=0.0)
	# btce_buyprice_ltc = models.FloatField(default=0.0)
	bitfinex_buyprice_ltc = models.FloatField(default=0.0)
	btcchina_buyprice_ltc = models.FloatField(default=0.0)
	huobi_buyprice_ltc = models.FloatField(default=0.0)
	created = models.DateTimeField(blank=True,default=datetime.datetime.now())

	def __unicode__(self):
		return '%s' % self.okcoin_buyprice

class Tradedate(models.Model):
	mtime = models.CharField(max_length=20, default='', db_index=True)
	price = models.FloatField(default=0.0)
	amount = models.FloatField(default=0.0)
	mtype = models.CharField(max_length=20, default='')
	created_day = models.CharField(max_length=20, default='')
	created = models.DateTimeField(blank=True,default=datetime.datetime.now())

	def __unicode__(self):
		return '%s' % self.price

class Tradedate_analysis(models.Model):
	buyorsell = models.CharField(max_length=20, default='')
	avg_price = models.FloatField(default=0.0)
	start_time = models.CharField(max_length=20, default='')
	end_time = models.CharField(max_length=20, default='')
	buy_amount = models.FloatField(default=0.0)
	sell_amount = models.FloatField(default=0.0)
	created = models.DateTimeField(blank=True,default=datetime.datetime.now())

	def __unicode__(self):
		return '%s' % self.buyorsell









