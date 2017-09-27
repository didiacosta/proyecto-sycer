"""
Django settings for sycer project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7#dyarww%k6f(y-w+jcxu^^eqfpy^=!^8dq=-289v9fx=pzlfg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)
# Application definition

TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors':[
                #'django.template.context_processors.request',
                'django.template.context_processors.media',
            ],
        },
    },
]
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)
GRAPPELLI_ADMIN_TITLE = 'SYCER'
#from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
#TEMPLATE_CONTEXT_PROCESSORS =  TCP + ('django.core.context_processors.request',)

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'departamento',
    'municipio',
    'accion',
    'aplicacion',
    'menu',
    'empresa',
    'asignacion_espacio',
    'usuario',
    'acceso',
    'accesoAccion',
    'tipoCertificado',
    'cliente',
    'empresaCliente',
    'certificado',
    'inspector',
    'empresaInspector',
    'dictamen',
    'dictamenDistribucion',
    'aspectoEvaluado',
    'evaluacionDictamen',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sycer.urls'

WSGI_APPLICATION = 'sycer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'sycer',                      
        'USER': 'root',                      
        'PASSWORD': 'santi10',         
        'HOST': '127.0.0.1',                 
        'PORT': '3607',                      
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])
#MEDIA_URL = '/media/'

LOGIN_URL = '/usuario/login/'
LOGOUT_URL = '/usuario/logout/'

#Configuracion de AWS


AWS_STORAGE_BUCKET_NAME = 'sycer'
AWS_ACCESS_KEY_ID = 'AKIAJJTRZP7GG53F3SJA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
