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
    'social.apps.django_app.default',
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

# https://docs.djangoproject.com/en/1.6/ref/settings/#std:setting-SESSION_EXPIRE_AT_BROWSER_CLOSE
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
TEMPLATE_CONTEXT_PROCESSORS = (
    "social.apps.django_app.context_processors.backends",
    "social.apps.django_app.context_processors.login_redirect",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    )

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
      'social.backends.twitter.TwitterOAuth',
      'django.contrib.auth.backends.ModelBackend',
  )
from misc_common.get_keys import init_keys
MISC_KEYS = init_keys(keyfile=APP_KEYFILE)

SOCIAL_AUTH_TWITTER_KEY = MISC_KEYS['social_auth_twitter_key']
SOCIAL_AUTH_TWITTER_SECRET = MISC_KEYS['social_auth_twitter_secret']
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/user/disconnected'


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

TWITTER_KEY = MISC_KEYS['twitter_key']
TWITTER_SECRET = MISC_KEYS['twitter_secret']

UNBABEL_USER = 'krc5kz'
UNBABEL_KEY = MISC_KEYS['unbabel_sandbox_key']

