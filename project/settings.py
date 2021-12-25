"""
Django settings for almatyqap project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from collections import OrderedDict
from pathlib import Path
import environ
from django.conf import global_settings
from django.utils.translation import ugettext_lazy as _

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u%wq6e$31uw9_w8t6mo0rz!+3w$0^n50+!+=!yzi9tcr2yw8)a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=False)

ALLOWED_HOSTS = ['localhost']

# Application definition

INSTALLED_APPS = [
    'apps.business',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mptt',
    'ckeditor',
    'ckeditor_uploader',
    'sorl.thumbnail',
    'topnotchdev.files_widget',
    'constance',
    'constance.backends.database',
    # 'debug_toolbar'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND' : 'django.template.backends.django.DjangoTemplates',
        'DIRS'    : [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS' : {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.business.services.main_processor'
            ],
            'builtins'          : [
                'apps.business.templatetags.lang'
            ]
        },

    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql',
        'NAME'    : env('DATABASE_NAME', default='almatyqap'),
        'USER'    : env('DATABASE_USER', default='almatyqap'),
        'PASSWORD': env('DATABASE_PASSWORD', default='o9H3j6Z5i85DP85'),
        'HOST'    : env('DATABASE_HOST', default='127.0.0.1'),
        'PORT'    : env('DATABASE_PORT', default=3306),
        "OPTIONS" : {"charset": "utf8mb4"}
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles/'),
]
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
CKEDITOR_UPLOAD_PATH = "uploads/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# i18n
LOCALE_PATHS = (
    os.path.join(os.path.dirname(__file__), 'language'),
)

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
LANGUAGE_CODE = 'ru'
LANGUAGES = [
    ('ru', 'Русский'),
    ('kk', 'Қазақща'),
]
CONSTANCE_ADDITIONAL_FIELDS = {
    'image_field': ['django.forms.ImageField', {'required': False}]
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_CONFIG = OrderedDict({
    'company_name'      : ('ТОО «Алматы Қап»', _('Название Компании'), str),
    'logo'              : (None, _('Логотип Компании'), 'image_field'),
    'big_pic_home'      : (None, _('Балшая картинка'), 'image_field'),
    'home_page_about_ru': ('У нас вы можете заказать коробки из картона любой сложности и конструкции в любом количестве от одной штуки до промышленной партии', _('главная страница о компании Русский'), str),
    'home_page_about_kz': ('У нас вы можете заказать коробки из картона любой сложности и конструкции в любом количестве от одной штуки до промышленной партии', _('главная страница о компании Казахсий'), str),
    'address'           : ('МИКРОРАЙОН КАЙРАТ, 167', _('Адрес'), str),
    'tel_number'        : ('170840013221', _('Номер Телефона'), str),
})
