#encoding=utf-8
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.db.models import Q

from btc.lib.okcoin import *
from btc.lib.huobi import *
from btc.lib.btcchina import *
from btc.lib.btceapi import *
from btc.lib.bitfinex import *
from btc import tasks
from models import *
from forms import *
import pprint
import os
import uuid
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


from json import dumps
import urllib2
import urllib


from django.core import serializers
import json
from django.utils.timezone import utc
import pytz

def multiply(request):
    x = int(request.GET.get('x'))
    y = int(request.GET.get('y'))

    retval = x * y
    response = {'status': 'success', 'retval': retval}
    return HttpResponse(dumps(response), mimetype='application/json')

def signout(request):
	logout(request)
	data = {}
	return HttpResponseRedirect(reverse('signin'))


@login_required
def setting(request):
	data={}	
	data['request']	= request
	if request.method=='POST':		
		request.user.userprofile.rate = request.POST.get('rate')
		request.user.userprofile.amount = request.POST.get('amount')
		request.user.userprofile.ltcamount = request.POST.get('ltcamount')

		request.user.userprofile.okcoin_key = request.POST.get('okcoin_key')
		request.user.userprofile.okcoin_secret = request.POST.get('okcoin_secret')
		request.user.userprofile.bitfinex_key = request.POST.get('bitfinex_key')
		request.user.userprofile.bitfinex_secret = request.POST.get('bitfinex_secret')

		request.user.userprofile.huobi_key = request.POST.get('huobi_key')
		request.user.userprofile.huobi_secret = request.POST.get('huobi_secret')
		# request.user.userprofile.btce_secret = request.POST.get('btce_secret')
		request.user.userprofile.btcchina_key = request.POST.get('btcchina_key')
		request.user.userprofile.btcchina_secret = request.POST.get('btcchina_secret')
		request.user.userprofile.save()
		return HttpResponseRedirect(reverse('setting'))
	return render_to_response('setting.html',data,context_instance=RequestContext(request))

@login_required
def btcsetting(request):
	data={}	
	data['request']	= request
	if request.method=='POST':
		request.user.userprofile.okCoin2bitfinex = request.POST.get('okCoin2bitfinex') 
		request.user.userprofile.bitfinex2okCoin = request.POST.get('bitfinex2okCoin')
		# request.user.userprofile.btce2bitfinex = request.POST.get('btce2bitfinex')
		# request.user.userprofile.bitfinex2btce = request.POST.get('bitfinex2btce')
		request.user.userprofile.okCoin2huobi = request.POST.get('okCoin2huobi')
		request.user.userprofile.huobi2okCoin = request.POST.get('huobi2okCoin')
		request.user.userprofile.okCoin2btcchina = request.POST.get('okCoin2btcchina')
		request.user.userprofile.btcchina2okCoin = request.POST.get('btcchina2okCoin')
		request.user.userprofile.huobi2btcchina = request.POST.get('huobi2btcchina')
		request.user.userprofile.btcchina2huobi = request.POST.get('btcchina2huobi')
		request.user.userprofile.huobi2bitfinex = request.POST.get('huobi2bitfinex')
		request.user.userprofile.bitfinex2huobi = request.POST.get('bitfinex2huobi')
		request.user.userprofile.bitfinex2btcchina = request.POST.get('bitfinex2btcchina')
		request.user.userprofile.btcchina2bitfinex = request.POST.get('btcchina2bitfinex')

		request.user.userprofile.save()
		return HttpResponseRedirect(reverse('btcsetting'))
	return render_to_response('btcsetting.html',data,context_instance=RequestContext(request))


@login_required
def ltcsetting(request):
	data={}	
	data['request']	= request
	if request.method=='POST':		
		# request.user.userprofile.ltcamount = request.POST.get('ltcamount')
		# request.user.userprofile.okCoin2BTCE = request.POST.get('okCoin2BTCE')
		request.user.userprofile.okCoin2bitfinex_ltc = request.POST.get('okCoin2bitfinex_ltc') 
		request.user.userprofile.bitfinex2okCoin_ltc = request.POST.get('bitfinex2okCoin_ltc')
		# request.user.userprofile.btce2bitfinex = request.POST.get('btce2bitfinex')
		# request.user.userprofile.bitfinex2btce = request.POST.get('bitfinex2btce')
		request.user.userprofile.okCoin2huobi_ltc = request.POST.get('okCoin2huobi_ltc')
		request.user.userprofile.huobi2okCoin_ltc = request.POST.get('huobi2okCoin_ltc')
		request.user.userprofile.okCoin2btcchina_ltc = request.POST.get('okCoin2btcchina_ltc')
		request.user.userprofile.btcchina2okCoin_ltc = request.POST.get('btcchina2okCoin_ltc')
		request.user.userprofile.huobi2btcchina_ltc = request.POST.get('huobi2btcchina_ltc')
		request.user.userprofile.btcchina2huobi_ltc = request.POST.get('btcchina2huobi_ltc')
		request.user.userprofile.huobi2bitfinex_ltc = request.POST.get('huobi2bitfinex_ltc')
		request.user.userprofile.bitfinex2huobi_ltc = request.POST.get('bitfinex2huobi_ltc')
		request.user.userprofile.bitfinex2btcchina_ltc = request.POST.get('bitfinex2btcchina_ltc')
		request.user.userprofile.btcchina2bitfinex_ltc = request.POST.get('btcchina2bitfinex_ltc')		
		request.user.userprofile.save()
		return HttpResponseRedirect(reverse('ltcsetting'))
	return render_to_response('ltcsetting.html',data,context_instance=RequestContext(request))



def signout(request):
	logout(request)
	return HttpResponseRedirect(reverse('signin'))

def signin(request):
	data={}
	data['request'] = request
	if request.user.is_authenticated():		
		return HttpResponseRedirect(request.GET.get('next',reverse('show')))
	
	if request.method=='GET':		
		return render_to_response('signin.html',data,context_instance=RequestContext(request))
	else:
		username = request.POST.get('username')
		password = request.POST.get('password')
		print username
		print password
		users = User.objects.filter(username=username)
		user_auth = authenticate(username=users[0].username,password=password)
		pprint.pprint(user_auth)
		login(request, user_auth)
		return HttpResponseRedirect(reverse('show'))
	return render_to_response('signin.html',data,context_instance=RequestContext(request))

@login_required
def show(request):
	data={}	
	data['request'] = request
	return render_to_response('show.html',data,context_instance=RequestContext(request))

@login_required
def getokcoininfo(request):
	result=[]
	user = Userprofile.objects.filter(user=request.user)[0]
	okcoin = OkCoin(user.okcoin_key.__str__(),user.okcoin_secret.__str__())
	g=tasks.okcoin_task_info.delay(okcoin,user.rate)
	re = g.get()
	result.append({'cny':re[0],'btc':re[1],'ltc':re[2]})
	return HttpResponse(json.dumps(result),mimetype="text/json")

@login_required
def gethuobiinfo(request):
	result=[]
	user = Userprofile.objects.filter(user=request.user)[0]
	huobi = HuoBi(user.huobi_key.__str__(), user.huobi_secret.__str__())
	g=tasks.huobi_task_info.delay(huobi,user.rate)
	re = g.get()
	result.append({'cny':re[0],'btc':re[1],'ltc':re[2]})
	return HttpResponse(json.dumps(result),mimetype="text/json")

@login_required
def getbtcchinainfo(request):
	result=[]
	user = Userprofile.objects.filter(user=request.user)[0]
	btcchina = BTCChina(user.btcchina_key.__str__(), user.btcchina_secret.__str__())
	g=tasks.btcchina_task_info.delay(btcchina,user.rate)
	re = g.get()
	result.append({'cny':re[0],'btc':re[1],'ltc':re[2]})
	return HttpResponse(json.dumps(result),mimetype="text/json")


@login_required
def getbtceinfo(request):
	result=[]
	user = Userprofile.objects.filter(user=request.user)[0]
	btce = api(user.btce_key.__str__(),user.btce_secret.__str__())
	g=tasks.btce_task_info.delay(btce)
	re = g.get()
	result.append({'usd':re[0],'btc':re[1],'ltc':re[2]})
	return HttpResponse(json.dumps(result),mimetype="text/json")

@login_required
def getbitfinexinfo(request):
	result=[]	
	user = Userprofile.objects.filter(user=request.user)[0]
	bfx = Bitfinex()
	bfx.key = user.bitfinex_key.__str__()
	bfx.secret = user.bitfinex_secret.__str__()
	g=tasks.bitfinex_task_info.delay(bfx)
	re = g.get()
	result.append({'usd':re[0],'btc':re[1],'ltc':re[2]})
	return HttpResponse(json.dumps(result),mimetype="text/json")


@login_required
def traderecode(request):
	data={}
	data['request'] = request
	recode=Btcexchange.objects.filter(exchange_user=request.user, order_id__gte=0, exchange_coin='btc').order_by('-created')
	data['recode'] = recode
	paginator = Paginator(recode,40)
	page = (int)(request.GET.get('page','1'))
	try:
		topics = paginator.page(page)
	except PageNotAnInteger:
		topics = paginator.page(1)
	except EmptyPage:
		topics = paginator.page(paginator.num_pages)
	data['topics'] = topics
	
	return render_to_response('traderecode.html',data,context_instance=RequestContext(request))

@login_required
def traderecodeltc(request):
	data={}
	data['request'] = request
	recode=Btcexchange.objects.filter(exchange_user=request.user, order_id__gte=0, exchange_coin='ltc').order_by('-created')
	data['recode'] = recode
	paginator = Paginator(recode,40)
	page = (int)(request.GET.get('page','1'))
	try:
		topics = paginator.page(page)
	except PageNotAnInteger:
		topics = paginator.page(1)
	except EmptyPage:
		topics = paginator.page(paginator.num_pages)
	data['topics'] = topics
	
	return render_to_response('traderecodeltc.html',data,context_instance=RequestContext(request))




@login_required
def showmacd(request):
	data={}	
	data['request'] = request
	return render_to_response('showmacd.html',data,context_instance=RequestContext(request))


@login_required
def getanalysis(request):
	data=Tradedate_analysis.objects.order_by('-created')[0:20]
	re1=[]
	re2=[]
	for item in data:
		# re1.append({'created':item.created.strftime("%Y-%m-%d %H:%M:%S %Z"), 'amount': item.buy_amount})
		if item.buyorsell == 'buy':
			re1.append({'created':item.created.strftime("%Y-%m-%d %H:%M:%S %Z"), 'amount': item.buy_amount*-1})
		else:
			re2.append({'created':item.created.strftime("%Y-%m-%d %H:%M:%S %Z"), 'amount': item.sell_amount})
	re1.reverse()
	re2.reverse()
	result=[re1,re2]
	return HttpResponse(json.dumps(result),mimetype="text/json")

@login_required
def getprice(request):
	user = Userprofile.objects.filter(id=1)
	user = user[0]
	rate = user.rate

	data=Pricebuysell.objects.order_by('-id')[0:10]
	re1 = []
	re2 = []
	re3 = []
	re4 = []
	

	for item in data:
		a='%.3f' % (item.okcoin_buyprice / rate)
		b='%.3f' % (item.huobi_buyprice / rate)
		c='%.3f' % (item.btcchina_buyprice / rate)
		d='%.3f' % item.bitfinex_buyprice

		a1='%.3f' % (item.okcoin_buyprice_ltc / rate)
		b1='%.3f' % (item.huobi_buyprice_ltc / rate)
		c1='%.3f' % (item.btcchina_buyprice_ltc / rate)
		d1='%.3f' % item.bitfinex_buyprice_ltc

		ok2huo = abs((item.okcoin_buyprice-item.huobi_buyprice) / max(item.okcoin_buyprice, item.huobi_buyprice)*100.0)
		ok2china = abs((item.btcchina_buyprice-item.okcoin_buyprice) / max(item.btcchina_buyprice, item.okcoin_buyprice)*100.0)
		ok2bfx = abs((item.okcoin_buyprice / rate - item.bitfinex_buyprice) / max(item.okcoin_buyprice / rate, item.bitfinex_buyprice)*100.0)
		huo2china = abs((item.huobi_buyprice - item.btcchina_buyprice) / max(item.huobi_buyprice, item.btcchina_buyprice)*100.0)
		huo2bfx = abs((item.huobi_buyprice /rate - item.bitfinex_buyprice) / max(item.huobi_buyprice /rate, item.bitfinex_buyprice)*100.0)
		china2bfx = abs((item.btcchina_buyprice /rate - item.bitfinex_buyprice) / max(item.btcchina_buyprice /rate, item.bitfinex_buyprice)*100.0)

		ok2huo_ltc = abs((item.okcoin_buyprice_ltc-item.huobi_buyprice_ltc) / max(item.okcoin_buyprice_ltc, item.huobi_buyprice_ltc)*100.0)
		ok2china_ltc = abs((item.btcchina_buyprice_ltc-item.okcoin_buyprice_ltc) / max(item.btcchina_buyprice_ltc, item.okcoin_buyprice_ltc)*100.0)
		ok2bfx_ltc = abs((item.okcoin_buyprice_ltc / rate - item.bitfinex_buyprice_ltc) / max(item.okcoin_buyprice_ltc / rate, item.bitfinex_buyprice_ltc)*100.0)
		huo2china_ltc = abs((item.huobi_buyprice_ltc - item.btcchina_buyprice_ltc) / max(item.huobi_buyprice_ltc, item.btcchina_buyprice_ltc)*100.0)
		huo2bfx_ltc = abs((item.huobi_buyprice_ltc /rate - item.bitfinex_buyprice_ltc) / max(item.huobi_buyprice_ltc /rate, item.bitfinex_buyprice_ltc)*100.0)
		china2bfx_ltc = abs((item.btcchina_buyprice_ltc /rate - item.bitfinex_buyprice_ltc) / max(item.btcchina_buyprice_ltc /rate, item.bitfinex_buyprice_ltc)*100.0)

		
		re1.append({'created':item.created.strftime("%Y-%m-%d %H:%M:%S %Z"), 'okcoin_buyprice': a, 'diff': diff1})
		re2.append({'created':item.created.strftime("%Y-%m-%d %H:%M:%S %Z"), 'huobi_buyprice': b, 'diff': diff2})
		re3.append({'created':item.created.strftime("%Y-%m-%d %H:%M:%S %Z"), 'btcchina_buyprice':c, 'diff': diff3})
		re4.append({'created':item.created.strftime("%Y-%m-%d %H:%M:%S %Z"), 'bitfinex_buyprice':d, 'diff': diff4})

		re5.append({'created':item.created.strftime("%Y-%m-%d %H:%M:%S %Z"), 'okcoin_buyprice_ltc':a1, 'diff': diff5})
		re6.append({'created':item.created.strftime("%Y-%m-%d %H:%M:%S %Z"), 'huobi_buyprice_ltc':b1, 'diff': diff6})
		re7.append({'created':item.created.strftime("%Y-%m-%d %H:%M:%S %Z"), 'btcchina_buyprice_ltc':c1, 'diff': diff7})
		re8.append({'created':item.created.strftime("%Y-%m-%d %H:%M:%S %Z"), 'bitfinex_buyprice_ltc':d1, 'diff': diff8})

	re1.reverse()
	re2.reverse()
	re3.reverse()
	re4.reverse()
	re5.reverse()
	re6.reverse()
	re7.reverse()
	re8.reverse()
	result=[re1,re2,re3,re4,re5,re6,re7,re8]
	return HttpResponse(json.dumps(result),mimetype="text/json")