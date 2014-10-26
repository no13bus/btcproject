DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


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