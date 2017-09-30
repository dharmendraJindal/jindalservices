import os
from manage import PROJECT_ROOT

from fabric.api import env, run

FAB_ENVIRONMENTS = env

#=============== ENV Settings=================

WEB_ENV = 'dev'

if WEB_ENV == "dev":
    print "Your env is [DEV]"

else:
    print "Your env is [LOCAL]"

#=============== Apps=================

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth2_provider',
    'compressor',
    'rest_framework',
    'django_extensions',
    'product',
    'authentication',
    'rest_framework.authtoken',
)

#======================================


#======== DJANGO Settings =====================

SITE_ID = "1"
SECRET_KEY = "68h(iy4+r@y2rh-t+*#s_-p1z%kfgdfe%$$#%nqf6lzw(9bh^&"

PROJECT_DIRNAME = PROJECT_ROOT

ROOT_URLCONF = "settings.urls"

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ALLOWED_HOSTS = ["*"]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'compressor.finders.CompressorFinder',
)
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, "static"),)
STATIC_URL = '/static/'

COMPRESS_ROOT = "static/CACHE"

MEDIA_ROOT = 'static/media'

STATIC_ROOT = PROJECT_ROOT + "assets/"

MEDIA_URL = STATIC_URL + "media/"

UPLOAD_ROOT = MEDIA_ROOT + "media/uploads/"
DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "static/media/downloads/")

COMPRESS_ENABLED = True
DEBUG = True

#==============================================

