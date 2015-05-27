"""
Django settings for r_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6ndth=l-2y%4mz4af0h(5x+sdx1+2fw%@2e+0&-8nenxr$vmpr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rango',
    # 'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'r_project.urls'

WSGI_APPLICATION = 'r_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ['RDS_DB_NAME'],
#         'USER': os.environ['RDS_USERNAME'],
#         'PASSWORD': os.environ['RDS_PASSWORD'],
#         'HOST': os.environ['RDS_HOSTNAME'],
#         'PORT': os.environ['RDS_PORT'],
#     }
# }

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
    # DEBUG = False
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    # DEBUG = True




# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


# STATIC_PATH = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Location of template files for rango
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

#media server for uploads
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



"""If you want more control over how the passwords are hashed, then in the settings.py
 add in tuple to specify the PASSWORD_HASHERS:

PASSWORD_HASHERS = (
'django.contrib.auth.hashers.PBKDF2PasswordHasher',
'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
)"""


LOGIN_URL = '/rango/login/'




#######put static files on Amazon s3
# pip install django-storages boto

# run requirements.txt

# ad storages to INSTALLED_APPS

# if not DEBUG:
#     AWS_STORAGE_BUCKET_NAME = 'avoaja-rango'
#     AWS_ACCESS_KEY_ID = 'AKIAJX53SKLH6CSK2YBA'
#     AWS_SECRET_ACCESS_KEY = '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'
#     STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#     S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
#     STATIC_URL = S3_URL


# STATIC_ROOT = os.path.join(
#                 os.path.dirname(
#                     os.path.dirname(
#                         os.path.abspath(__file__)
#                         )
#                     ), 
#                     'static'
#                 )