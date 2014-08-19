"""
Django settings for base project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from sys import path

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Adding apps subdirectory to the path for later imports
path.append('{}/apps'.format(BASE_DIR))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@=9iu=a3gi#w&w%!y505op$99__#iw@9ei(lq)2*zkcgv0wu)x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['twitterfishing.herokuapp.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'south',

    'core',
    'fish',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'base.urls'

WSGI_APPLICATION = 'base.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'twitterfishing',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    }
}
import dj_database_url
DATABASES['default'] = dj_database_url.config()
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

AUTH_USER_MODEL = 'core.Account'

# https://docs.djangoproject.com/en/1.6/ref/settings/#std:setting-SESSION_EXPIRE_AT_BROWSER_CLOSE
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'templates/assets'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

TWITTER_KEY='E7EkZcp8icFFm04GEErVRlef2'
TWITTER_SECRET='3ka8meqx3dGFeYstotosEnTZEGtBFrSKUh0L9gN5LzekchHUDb'
ACCESS_KEY='2327970060-8Y3fWsSwMXYp9IchXB9G5eULRAS2F2dPI6gh2dc'
ACCESS_SECRET='VYgIBByq4NJlGtCavG8pvex4ktAUJGSga7RI8U61os4EH'

UNBABEL_USER = 'krc5kz'
UNBABEL_KEY = 'b092c64fc41fcb2fd7273dac436a5575e560e201'

