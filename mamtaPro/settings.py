"""
Django settings for mamtaPro project.

all code updated to django 4.2
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_@^6lnu4*+t_1qazvxdfn*k)treogq7h!r!e=p0*0pcp$l!j&&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mamtaApp',
    'pwa',
    'invoice',
    'attendance',
    'stdimage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mamtaPro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mamtaPro.wsgi.application'

#
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mamtaguwahati',
#         'HOST': 'localhost',
#         'PORT': '3306',
#         'USER': 'root',
#         'PASSWORD': 'pass',
#     }
# }




# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # '/var/www/static/',
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")

PWA_APP_NAME = 'A123DACN'
PWA_APP_DESCRIPTION = "Credit Management System."
PWA_APP_THEME_COLOR = '#2196f3'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_START_URL = '/login/'
PWA_APP_ICONS = [
    {
        "src": "static/sw/images/48.png",
        "sizes": "48x48",
        "type": "image/png"
    },
    {
        "src": "static/sw/images/72.png",
        "sizes": "72x72",
        "type": "image/png"
    },
    {
        "src": "static/sw/images/96.png",
        "sizes": "96x96",
        "type": "image/png"
    },
    {
        "src": "static/sw/images/144.png",
        "sizes": "144x144",
        "type": "image/png"
    },
    {
        "src": "static/sw/images/192.png",
        "sizes": "192x192",
        "type": "image/png"
    },
    {
        "src": "static/sw/images/512.png",
        "sizes": "512x512",
        "type": "image/png"
    }
]

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'mamtaApp', '../static/sw/sw.js')
SESSION_COOKIE_AGE = 30*60
SESSION_SAVE_EVERY_REQUEST = True
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

CSRF_TRUSTED_ORIGINS = [
    'https://a123dacn.in',
    'https://www.a123dacn.in'
]
