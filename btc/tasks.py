#encoding=utf-8
from __future__ import absolute_import

from celery import shared_task
# from celery.task import task
from btcproject import celery_app

from btc.lib.okcoin import *
from btc.lib.btceapi import *
from btc.lib.bitfinex import *
from btc.lib.huobi import *
from btc.lib.btcchina import *


from celery import Celery,platforms,group
import time
import pprint
import datetime

from btc.models import *
from datetime import timedelta
from django.utils.timezone import utc
from django.conf import settings

import logging
import logging.handlers

from mailer import Mailer
from mailer import Message



LOG_FILE = 'btc_celery.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024*20, backupCount = 10)
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)
logger = logging.getLogger('btc_celery')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

@celery_app.task
def send_btc_mail(subjectstring, messagestring):
	message = Message(From=settings.MAILSENDER,To=settings.TOLIST, charset="utf-8")
	message.Subject = subjectstring
	message.Html = messagestring
	mysender = Mailer(host=settings.MAILHOST, pwd=settings.MAILPWD, usr=settings.MAILSENDER)
	mysender.send(message)

@celery_app.task
def set_bool_task():
	if settings.SENDBOOL == False:
		logger.debug('set_bool is seted to true')
		settings.SENDBOOL = True

@celery_app.task
def bitfinex_task_btc(bfx):
	payload = {}
	book = bfx.book(payload)
	bitfinex_seller_price = float(book['asks'][1]['price'])
	bitfinex_buyer_price = float(book['bids'][1]['price'])
	bitfinex_buyer_price_done = float(book['asks'][5]['price'])
	bitfinex_seller_price_done = float(book['bids'][5]['price'])
	return [bitfinex_seller_price, bitfinex_buyer_price, bitfinex_seller_price_done, bitfinex_buyer_price_done]

@celery_app.task
def bitfinex_task_ltc(bfx):
	payload = {}
	ltc_book = bfx.book(payload,'ltcusd')
	bitfinex_seller_price_ltc = float(ltc_book['asks'][1]['price'])
	bitfinex_buyer_price_ltc = float(ltc_book['bids'][1]['price'])
	bitfinex_buyer_price_ltc_done = float(ltc_book['bids'][5]['price'])
	bitfinex_seller_price_ltc_done = float(ltc_book['asks'][5]['price'])
	return [bitfinex_seller_price_ltc, bitfinex_buyer_price_ltc, bitfinex_seller_price_ltc_done, bitfinex_buyer_price_ltc_done]

@celery_app.task
def bitfinex_task_info(bfx):
	user_info = bfx.balances()
	if [i['amount'] for i in user_info if i['type']=='exchange' and i['currency']=='usd']:
		usd = float([i['amount'] for i in user_info if i['type']=='exchange' and i['currency']=='usd'][0])
	else:
		usd = 0.0
	if [i['amount'] for i in user_info if i['type']=='exchange' and i['currency']=='ltc']:
		ltc = float([i['amount'] for i in user_info if i['type']=='exchange' and i['currency']=='ltc'][0])
	else:
		ltc = 0.0
	if [i['amount'] for i in user_info if i['type']=='exchange' and i['currency']=='btc']:
		btc = float([i['amount'] for i in user_info if i['type']=='exchange' and i['currency']=='btc'][0])
	else:
		btc = 0.0
	return [usd,btc,ltc]


@celery_app.task
def btce_task_btc(btce):
	de = btce.get_Depth()
	btce_seller_price = de['bids'][1][0]
	btce_buyer_price = de['asks'][1][0]
	btce_seller_price_done = de['bids'][5][0]
	btce_buyer_price_done = de['asks'][5][0]
	return [btce_seller_price, btce_buyer_price, btce_seller_price_done, btce_buyer_price_done]

@celery_app.task
def btce_task_ltc(btce):
	ltc_de = btce.get_Depth('ltc_usd')
	btce_seller_price_ltc = ltc_de['bids'][1][0]
	btce_buyer_price_ltc = ltc_de['asks'][1][0]
	btce_seller_price_ltc_done = ltc_de['bids'][5][0]
	btce_buyer_price_ltc_done = ltc_de['asks'][5][0]
	return [btce_seller_price_ltc, btce_buyer_price_ltc, btce_seller_price_ltc_done, btce_buyer_price_ltc_done]

@celery_app.task
def btce_task_info(btce):
	user_info = btce.getInfo()
	usd = user_info['return']['funds']['usd']
	btc = user_info['return']['funds']['btc']
	ltc = user_info['return']['funds']['ltc']
	return [usd,btc,ltc]

@celery_app.task
def okcoin_task_btc(okcoin,rate):
	de = okcoin.get_depth()
	okcoin_seller_price = de['asks'][-1][0]
	okcoin_buyer_price = de['bids'][1][0]
	okcoin_seller_price_done = de['asks'][-5][0]
	okcoin_buyer_price_done = de['bids'][5][0]
	return [okcoin_seller_price, okcoin_buyer_price, okcoin_seller_price_done, okcoin_buyer_price_done]

@celery_app.task
def okcoin_task_ltc(okcoin,rate):
	ltc_de = okcoin.get_depth_ltc()
	okcoin_seller_price_ltc = ltc_de['asks'][-1][0]
	okcoin_buyer_price_ltc = ltc_de['bids'][1][0]
	okcoin_seller_price_ltc_done = ltc_de['asks'][-5][0]
	okcoin_buyer_price_ltc_done = ltc_de['bids'][5][0]
	return [okcoin_seller_price_ltc, okcoin_buyer_price_ltc, okcoin_seller_price_ltc_done, okcoin_buyer_price_ltc_done]

@celery_app.task
def okcoin_task_info(okcoin,rate):
	user_info = okcoin.get_account()
	cny = float(user_info['info']['funds']['free']['cny'])
	ltc = float(user_info['info']['funds']['free']['ltc'])
	btc = float(user_info['info']['funds']['free']['btc'])
	return [cny,btc,ltc]

@celery_app.task
def huobi_task_btc(huobi,rate):
	de = huobi.get_depth('btc')
	huobi_seller_price = float(de['asks'][-1][0])
	huobi_buyer_price = float(de['bids'][1][0])
	huobi_buyer_price_done = float(de['bids'][5][0])
	huobi_seller_price_done = float(de['asks'][-5][0])
	return [huobi_seller_price, huobi_buyer_price, huobi_seller_price_done, huobi_buyer_price_done]

@celery_app.task
def huobi_task_ltc(huobi,rate):
	ltc_de = huobi.get_depth('ltc')
	huobi_seller_price_ltc = float(ltc_de['asks'][-1][0])
	huobi_buyer_price_ltc = float(ltc_de['bids'][1][0])
	huobi_buyer_price_ltc_done = float(ltc_de['bids'][5][0])
	huobi_seller_price_ltc_done = float(ltc_de['asks'][-5][0])
	return [huobi_seller_price_ltc, huobi_buyer_price_ltc, huobi_seller_price_ltc_done, huobi_buyer_price_ltc_done]

@celery_app.task
def huobi_task_info(huobi,rate):
	user_info = huobi.get_account_info()
	cny = float(user_info['available_cny_display']) if 'available_cny_display' in user_info else 0.0
	ltc = float(user_info['available_ltc_display']) if 'available_ltc_display' in user_info else 0.0
	btc = float(user_info['available_btc_display']) if 'available_btc_display' in user_info else 0.0
	return [cny,btc,ltc]

### http.cannot requests 
@celery_app.task
def btcchina_task_btc(btcchina,rate):
	de = btcchina.get_depth()	
	btcchina_seller_price = de['asks'][-1][0]
	btcchina_buyer_price = de['bids'][1][0]
	btcchina_buyer_price_done = de['bids'][3][0]
	btcchina_seller_price_done = de['asks'][-3][0]
	return [btcchina_seller_price, btcchina_buyer_price, btcchina_seller_price_done, btcchina_buyer_price_done]


@celery_app.task
def btcchina_task_ltc(btcchina,rate):
	ltc_de = btcchina.get_depth('ltccny')	
	btcchina_seller_price_ltc = ltc_de['asks'][-1][0]
	btcchina_buyer_price_ltc = ltc_de['bids'][1][0]
	btcchina_buyer_price_ltc_done = ltc_de['bids'][3][0]
	btcchina_seller_price_ltc_done = ltc_de['asks'][-3][0]
	return [btcchina_seller_price_ltc, btcchina_buyer_price_ltc, btcchina_seller_price_ltc_done, btcchina_buyer_price_ltc_done]


@celery_app.task
def btcchina_task_info(bc,rate):
	user_info = bc.get_account_info()
	cny = user_info['balance']['cny']['amount']
	ltc = user_info['balance']['ltc']['amount']
	btc = user_info['balance']['btc']['amount']
	cny = float(cny)
	ltc = float(ltc)
	btc = float(btc)
	return [cny,btc,ltc]



@celery_app.task
def insert_buy_info(okcoin_buyprice,huobi_buyprice,btcchina_buyprice,bitfinex_buyprice,okcoin_buyprice_ltc,huobi_buyprice_ltc,btcchina_buyprice_ltc,bitfinex_buyprice_ltc,created):
	now = datetime.datetime.utcnow().replace(tzinfo=utc)
	p = Pricebuysell(okcoin_buyprice=okcoin_buyprice,huobi_buyprice=huobi_buyprice,
		btcchina_buyprice=btcchina_buyprice, bitfinex_buyprice=bitfinex_buyprice,
		okcoin_buyprice_ltc=okcoin_buyprice_ltc,huobi_buyprice_ltc=huobi_buyprice_ltc,
		btcchina_buyprice_ltc=btcchina_buyprice_ltc, bitfinex_buyprice_ltc=bitfinex_buyprice_ltc,created=now)
	p.save()


####实时抓取交易价格 并入mysql库 为了将其在前台显示出来
@celery_app.task
def user_trade():
	#### admin's settings
	user = Userprofile.objects.filter(id=1)
	user = user[0]
	rate = user.rate
	amount = user.amount
	ltcamount = user.ltcamount
	auto_trade = user.auto_trade
	user_id = user.user.id

	okcoin2bitfinex = user.okCoin2bitfinex
	bitfinex2okcoin = user.bitfinex2okCoin
	okcoin2huobi = user.okCoin2huobi
	huobi2okcoin = user.huobi2okCoin
	okcoin2btcchina = user.okCoin2btcchina
	btcchina2okcoin = user.btcchina2okCoin
	huobi2btcchina = user.huobi2btcchina
	btcchina2huobi = user.btcchina2huobi
	huobi2bitfinex = user.huobi2bitfinex
	bitfinex2huobi = user.bitfinex2huobi
	bitfinex2btcchina = user.bitfinex2btcchina
	btcchina2bitfinex = user.btcchina2bitfinex

	okcoin2bitfinex_ltc = user.okCoin2bitfinex_ltc
	bitfinex2okcoin_ltc = user.bitfinex2okCoin_ltc
	okcoin2huobi_ltc = user.okCoin2huobi_ltc
	huobi2okcoin_ltc = user.huobi2okCoin_ltc
	okcoin2btcchina_ltc = user.okCoin2btcchina_ltc
	btcchina2okcoin_ltc = user.btcchina2okCoin_ltc
	huobi2btcchina_ltc = user.huobi2btcchina_ltc
	btcchina2huobi_ltc = user.btcchina2huobi_ltc
	huobi2bitfinex_ltc = user.huobi2bitfinex_ltc
	bitfinex2huobi_ltc = user.bitfinex2huobi_ltc
	bitfinex2btcchina_ltc = user.bitfinex2btcchina_ltc
	btcchina2bitfinex_ltc = user.btcchina2bitfinex_ltc

	##
	okcoin = OkCoin(user.okcoin_key.__str__(),user.okcoin_secret.__str__())
	bfx = Bitfinex()
	bfx.key = user.bitfinex_key.__str__()
	bfx.secret = user.bitfinex_secret.__str__()
	huobi = HuoBi(user.huobi_key.__str__(), user.huobi_secret.__str__())
	btcchina = BTCChina(user.btcchina_key.__str__(), user.btcchina_secret.__str__())


	g=group(bitfinex_task_btc.s(bfx), huobi_task_btc.s(huobi, rate),
			btcchina_task_btc.s(btcchina, rate), okcoin_task_btc.s(okcoin, rate),
			bitfinex_task_ltc.s(bfx), huobi_task_ltc.s(huobi, rate),
			btcchina_task_ltc.s(btcchina, rate), okcoin_task_ltc.s(okcoin, rate),
			bitfinex_task_info.s(bfx),huobi_task_info.s(huobi, rate),btcchina_task_info.s(btcchina, rate),okcoin_task_info.s(okcoin, rate))

	result = g().get()

	okcoin_buyprice_btc = result[3][1]
	huobi_buyprice_btc = result[1][1]
	btcchina_buyprice_btc = result[2][1]
	bitfinex_buyprice_btc = result[0][1]
	okcoin_sellprice_btc = result[3][0]
	huobi_sellprice_btc = result[1][0]
	btcchina_sellprice_btc = result[2][0]
	bitfinex_sellprice_btc = result[0][0]
	okcoin_buyprice_ltc = result[7][1]
	huobi_buyprice_ltc = result[5][1]
	btcchina_buyprice_ltc = result[6][1]
	bitfinex_buyprice_ltc = result[4][1]
	okcoin_sellprice_ltc = result[7][0]
	huobi_sellprice_ltc = result[5][0]
	btcchina_sellprice_ltc = result[6][0]
	bitfinex_sellprice_ltc = result[4][0]
	
	created = datetime.datetime.utcnow().replace(tzinfo=utc)
	insert_buy_info.delay(okcoin_buyprice_btc,huobi_buyprice_btc,btcchina_buyprice_btc,bitfinex_buyprice_btc,
		okcoin_buyprice_ltc,huobi_buyprice_ltc,btcchina_buyprice_ltc,bitfinex_buyprice_ltc,created)

@celery_app.task
def tradedate():
	user = Userprofile.objects.filter(id=1)
	user = user[0]
	rate = user.rate
	amount = user.amount
	ltcamount = user.ltcamount
	auto_trade = user.auto_trade
	user_id = user.user.id
	huobi = HuoBi(user.huobi_key.__str__(), user.huobi_secret.__str__())
	huobi_j = huobi.get_trades_history('btc')
	
	trade_dates = huobi_j['trades']
	for data in trade_dates:
		price = data['price']
		amount = data['amount']
		mtype = data['type']
		created_day = datetime.datetime.now().strftime("%Y-%m-%d")
		mtime = '%s %s' % (created_day, data['time'])
		now = datetime.datetime.utcnow().replace(tzinfo=utc)
		td = Tradedate.objects.filter(mtime=mtime,price=price,amount=amount,mtype=mtype)
		if not td:
			trade_item = Tradedate(mtime=mtime,price=price,amount=amount,mtype=mtype,created=now)
			trade_item.save()

@celery_app.task
def tradedate_analysis():
	t_delta = datetime.timedelta(seconds=60)
	nowdate = datetime.datetime.now()
	start_time = nowdate.strftime("%Y-%m-%d %H:%M:%S")
	end_time = (nowdate - t_delta).strftime("%Y-%m-%d %H:%M:%S")
	td = Tradedate.objects.filter(mtime__gte=end_time, mtime__lte=start_time).order_by('-mtime')
	if not td:
		return
	
	avg_price = sum([item.price for item in td]) / len(td)
	avg_price = round(avg_price,4)
	buy_data = td.filter(mtype=u'买入')
	buy_amount = sum([item.amount for item in buy_data])
	buy_amount = round(buy_amount,4)
	sell_data = td.filter(mtype=u'卖出')
	sell_amount = sum([item.amount for item in sell_data])
	sell_amount = round(sell_amount,4)
	if buy_amount > sell_amount:
		buyorsell = 'buy'
	else:
		buyorsell = 'sell'
	if not Tradedate_analysis.objects.filter(start_time=start_time,end_time=end_time):
		now = datetime.datetime.utcnow().replace(tzinfo=utc)
		ta = Tradedate_analysis(buyorsell=buyorsell,avg_price=avg_price,start_time=start_time,end_time=end_time,
			buy_amount=buy_amount,sell_amount=sell_amount,created=now)
		ta.save()



