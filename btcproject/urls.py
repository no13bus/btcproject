from django.conf.urls import patterns, include, url

from django.contrib import admin
from btc.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples: ooxxbtc
    # url(r'^$', 'btcproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^signin/$', signin,name='signin'),
    url(r'^signout/$', signout,name='signout'),
    url(r'^setting/$',setting,name='setting'),
    url(r'^ltcsetting/$',ltcsetting,name='ltcsetting'),
    url(r'^btcsetting/$',btcsetting,name='btcsetting'),
    url(r'^show/$',show,name='show'),
    url(r'^multiply/$',multiply,name='multiply'),
    url(r'^getprice/$',getprice,name='getprice'),
    url(r'^getokcoininfo/$',getokcoininfo,name='getokcoininfo'),
    url(r'^gethuobiinfo/$',gethuobiinfo,name='gethuobiinfo'),
    url(r'^getbtcchinainfo/$',getbtcchinainfo,name='getbtcchinainfo'),
    url(r'^getbtceinfo/$',getbtceinfo,name='getbtceinfo'),
    url(r'^getbitfinexinfo/$',getbitfinexinfo,name='getbitfinexinfo'),
    url(r'^getanalysis/$',getanalysis,name='getanalysis'),
    url(r'^showmacd/$',showmacd,name='showmacd'),
    url(r'^/$', show,name='show'),

    
)
