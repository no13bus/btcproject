"""
Django settings for btcproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Celery settings

# BROKER_URL = 'redis://localhost:6379/0'

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
# CELERY_ACCEPT_CONTENT = ['json']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#-rqr0pyq=fj3awrq2*4@k*ol*7oo#7wrkeu$@tms1z8)x8yf3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

CACHE_BACKEND = 'locmem:///'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'btc',
    'gunicorn',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
)

ROOT_URLCONF = 'btcproject.urls'

WSGI_APPLICATION = 'btcproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'btc',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'root',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
)
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_ROOT = '/home/btcproject/static'


STATIC_URL = '/static/'

LOGIN_URL = '/signin/'

# from btc.tasks import *
# from datetime import timedelta
# from models import *


####celery settings
import djcelery
from datetime import timedelta

djcelery.setup_loader()
CELERYBEAT_SCHEDULE = {
    'trade-every-6-seconds': {
        'task': 'btc.tasks.user_trade',
        'schedule': timedelta(seconds=4),
    },
    'trade-date': {
        'task': 'btc.tasks.tradedate',
        'schedule': timedelta(seconds=10),
    },
    'trade-date-analysis': {
        'task': 'btc.tasks.tradedate_analysis',
        'schedule': timedelta(seconds=60),
    },
}


CELERYD_POOL_RESTARTS = True

#####dev enviriment or deploy enviriment
import socket

if socket.gethostname() == 'jqh-virtual-machine':
    try:
        from settings_dev import *
    except ImportError:
        pass
if socket.gethostname() == 'no13busdeMacBook-Air.local':
    try:
        from settings_dev import *
    except ImportError:
        pass

