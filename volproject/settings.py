"""
Django settings for volproject project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
from os import getenv
from dotenv import load_dotenv
from pathlib import Path
import django_heroku

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "http://localhost:3000",
    "https://wordlearner.onrender.com",
    'https://MDjudge-bot.gary940610.repl.co',
    'http://172.31.128.33',
    'https://wordlearner.tech',
    'https://216.144.250.150',
    'https://69.162.124.226',
    'https://69.162.124.227',
    'https://69.162.124.228',
    'https://69.162.124.229',
    'https://69.162.124.230',
    'https://69.162.124.231',
    'https://69.162.124.232',
    'https://69.162.124.233',
    'https://69.162.124.234',
    'https://69.162.124.235',
    'https://69.162.124.236',
    'https://69.162.124.237',
    'https://63.143.42.242',
    'https://63.143.42.243',
    'https://63.143.42.244',
    'https://63.143.42.245',
    'https://63.143.42.246',
    'https://63.143.42.247',
    'https://63.143.42.248',
    'https://63.143.42.249',
    'https://63.143.42.250',
    'https://63.143.42.251',
    'https://63.143.42.252',
    'https://63.143.42.253',
    'https://216.245.221.82',
    'https://216.245.221.83',
    'https://216.245.221.84',
    'https://216.245.221.85',
    'https://216.245.221.86',
    'https://216.245.221.87',
    'https://216.245.221.88',
    'https://216.245.221.89',
    'https://216.245.221.90',
    'https://216.245.221.91',
    'https://216.245.221.92',
    'https://216.245.221.93',
    'https://208.115.199.18',
    'https://208.115.199.19',
    'https://208.115.199.20',
    'https://208.115.199.21',
    'https://208.115.199.22',
    'https://208.115.199.23',
    'https://208.115.199.24',
    'https://208.115.199.25',
    'https://208.115.199.26',
    'https://208.115.199.27',
    'https://208.115.199.28',
    'https://208.115.199.29',
    'https://208.115.199.30',
    'https://216.144.248.18',
    'https://216.144.248.19',
    'https://216.144.248.20',
    'https://216.144.248.21',
    'https://216.144.248.22',
    'https://216.144.248.23',
    'https://216.144.248.24',
    'https://216.144.248.25',
    'https://216.144.248.26',
    'https://216.144.248.27',
    'https://216.144.248.28',
    'https://216.144.248.29',
    'https://216.144.248.30',
    'https://46.137.190.132',
    'https://122.248.234.23',
    'https://167.99.209.234',
    'https://178.62.52.237',
    'https://54.79.28.129',
    'https://54.94.142.218',
    'https://104.131.107.63',
    'https://54.67.10.127',
    'https://54.64.67.106',
    'https://159.203.30.41',
    'https://46.101.250.135',
    'https://18.221.56.27',
    'https://52.60.129.180',
    'https://159.89.8.111',
    'https://146.185.143.14',
    'https://139.59.173.249',
    'https://165.227.83.148',
    'https://128.199.195.156',
    'https://138.197.150.151',
    'https://34.233.66.117',
    'https://52.70.84.165',
    'https://54.225.82.45',
    'https://69.162.124.224',
    'https://63.143.42.240',
    'https://216.245.221.80',
    'https://208.115.199.16',
    'https://216.144.248.16',
]


# Application definition
CORS_ORIGIN_ALLOW_ALL=False

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djoser',

    'vols',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://wordlearner.onrender.com",
    'https://MDjudge-bot.gary940610.repl.co',
    'http://172.31.128.33',
    'https://wordlearner.tech',
    'https://216.144.250.150',
    'https://69.162.124.226',
    'https://69.162.124.227',
    'https://69.162.124.228',
    'https://69.162.124.229',
    'https://69.162.124.230',
    'https://69.162.124.231',
    'https://69.162.124.232',
    'https://69.162.124.233',
    'https://69.162.124.234',
    'https://69.162.124.235',
    'https://69.162.124.236',
    'https://69.162.124.237',
    'https://63.143.42.242',
    'https://63.143.42.243',
    'https://63.143.42.244',
    'https://63.143.42.245',
    'https://63.143.42.246',
    'https://63.143.42.247',
    'https://63.143.42.248',
    'https://63.143.42.249',
    'https://63.143.42.250',
    'https://63.143.42.251',
    'https://63.143.42.252',
    'https://63.143.42.253',
    'https://216.245.221.82',
    'https://216.245.221.83',
    'https://216.245.221.84',
    'https://216.245.221.85',
    'https://216.245.221.86',
    'https://216.245.221.87',
    'https://216.245.221.88',
    'https://216.245.221.89',
    'https://216.245.221.90',
    'https://216.245.221.91',
    'https://216.245.221.92',
    'https://216.245.221.93',
    'https://208.115.199.18',
    'https://208.115.199.19',
    'https://208.115.199.20',
    'https://208.115.199.21',
    'https://208.115.199.22',
    'https://208.115.199.23',
    'https://208.115.199.24',
    'https://208.115.199.25',
    'https://208.115.199.26',
    'https://208.115.199.27',
    'https://208.115.199.28',
    'https://208.115.199.29',
    'https://208.115.199.30',
    'https://216.144.248.18',
    'https://216.144.248.19',
    'https://216.144.248.20',
    'https://216.144.248.21',
    'https://216.144.248.22',
    'https://216.144.248.23',
    'https://216.144.248.24',
    'https://216.144.248.25',
    'https://216.144.248.26',
    'https://216.144.248.27',
    'https://216.144.248.28',
    'https://216.144.248.29',
    'https://216.144.248.30',
    'https://46.137.190.132',
    'https://122.248.234.23',
    'https://167.99.209.234',
    'https://178.62.52.237',
    'https://54.79.28.129',
    'https://54.94.142.218',
    'https://104.131.107.63',
    'https://54.67.10.127',
    'https://54.64.67.106',
    'https://159.203.30.41',
    'https://46.101.250.135',
    'https://18.221.56.27',
    'https://52.60.129.180',
    'https://159.89.8.111',
    'https://146.185.143.14',
    'https://139.59.173.249',
    'https://165.227.83.148',
    'https://128.199.195.156',
    'https://138.197.150.151',
    'https://34.233.66.117',
    'https://52.70.84.165',
    'https://54.225.82.45',
    'https://69.162.124.224',
    'https://63.143.42.240',
    'https://216.245.221.80',
    'https://208.115.199.16',
    'https://216.144.248.16',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'volproject.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'volproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rsknzraf',
        'USER': 'rsknzraf',
        'PASSWORD': getenv('PASSWORD'),
        'HOST': 'tiny.db.elephantsql.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

django_heroku.settings(locals())
