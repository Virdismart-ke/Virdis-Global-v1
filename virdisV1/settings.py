"""
Django settings for virdis project.
Generated by 'django-admin startproject' using Django 3.1.6.
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = '_ddyqu_(vf$c6*ejoap-!y)1@1z)2m-jirhci%k#9f@sn=a77e'
DEBUG = True
ALLOWED_HOSTS = ["virdis.co.ke","127.0.0.1","*"]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Accounts',
    'virdisV1.home',
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

ROOT_URLCONF = 'virdisV1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        BASE_DIR / 'Accounts/templates/',
        BASE_DIR / 'virdisV1/home/templates/',
            BASE_DIR / 'Asserts/templates/',
        ],
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

WSGI_APPLICATION = 'virdisV1.wsgi.application'
AUTH_USER_MODEL = "Accounts.Virdismart"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
# email configs
EMAIL_HOST = "mail.virdis.co.ke"
EMAIL_HOST_USER = "mailer@virdis.co.ke"
EMAIL_HOST_PASSWORD="J93Z)cvs5*kN7I"
EMAIL_HOST_PORT = 465
EMAIL_USE_TLS = True

STATICFILES_DIRS = [
    BASE_DIR / 'Accounts/static/',
    BASE_DIR / 'Asserts/static/',
    BASE_DIR / 'Home/static/',
]
STATIC_ROOT = BASE_DIR / "STATIC_ROOT/"
MEDIA_ROOT = BASE_DIR / "MEDIA_ROOT/"

STATIC_URL = '/static/'