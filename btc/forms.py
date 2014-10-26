#encoding=utf-8
from django import forms
from models import *

class SigninForm(forms.Form):
	# forms.TextInput(attrs={'style':'border:1px solid #ccc;'}))
	email=forms.EmailField(required=True,error_messages={'required':u'邮箱必须','invalid':u'请输入正确的邮箱'},widget=forms.TextInput(attrs={'id':'email','class':'input-xlarge'}))
	password=forms.CharField(required=True,error_messages={'required':u'密码必须'},widget=forms.PasswordInput(attrs={'id':'password','class':'input-xlarge'}))


class SettingForm(forms.Form):
	#required=False必须要加上required默认是true
	signature=forms.CharField(required=False,error_messages={'max_length':u'个人签名过长'},widget=forms.TextInput(attrs={'id':'signature','class':'input-xlarge'}))
	location=forms.CharField(required=False,error_messages={'max_length':u'不合适的城市名字'},widget=forms.TextInput(attrs={'id':'location','class':'input-xlarge'}))
	website=forms.URLField(required=False,error_messages={'invalid':u'无效的网址'},widget=forms.TextInput(attrs={'id':'website','class':'input-xlarge'}))
	douban=forms.CharField(required=False,widget=forms.TextInput(attrs={'id':'douban','class':'input-xlarge'}))
	github=forms.CharField(required=False,widget=forms.TextInput(attrs={'id':'github','class':'input-xlarge'}))
	self_intro=forms.CharField(required=False,error_messages={'max_length':u'介绍太长'},widget=forms.Textarea(attrs={'id':'self_intro','class':'input-xlarge','rows':'10'}))

class BtcexchangeForm(forms.Form):
	btcamount = forms.FloatField(required=True,error_messages={'required':u'btcamount必须'})
	price = forms.FloatField(required=True,error_messages={'required':u'price必须'})
	exchange_type = forms.IntegerField(required=True,error_messages={'required':u'exchange_type必须'})
	website = forms.CharField(required=True,error_messages={'required':u'website必须'})
	exchange_coin = forms.CharField(required=True,error_messages={'required':u'exchange_coin必须'})