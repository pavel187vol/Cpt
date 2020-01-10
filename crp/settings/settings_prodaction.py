from .base import *

DEBUG = True
ADMINS = (
    ('Pavel V', 'pavel.voloscovich@gmail.com'),
)


ALLOWED_HOSTS = ['frozen-mesa-66627.herokuapp.com']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'crp',
       'USER': 'rood',
       'PASSWORD': 'zhelezo',
       'HOST' : '127.0.0.1',
       'PORT' : '5432',
   }
}


import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
