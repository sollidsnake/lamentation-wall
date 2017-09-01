"""
Django settings for lamentation_wall project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# dot env
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True

TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR,'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',

        ],
    },
},] 


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'index_board',
    'social_django',
    'compressor',
    'easy_timezones',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'easy_timezones.middleware.EasyTimezoneMiddleware',

)
ROOT_URLCONF = 'lamentation_wall.urls'

GEOIP_DATABASE = os.path.join(BASE_DIR, 'tz', 'GeoLiteCity.dat')
GEOIPV6_DATABASE = os.path.join(BASE_DIR, 'tz', 'GeoLiteCityv6.dat')

# RECAPTCHA_PUBLIC_KEY = '6LdD1i4UAAAAADN92ZaYGTblIF9W6nuzye1kytHn'
# RECAPTCHA_PRIVATE_KEY = '6LdD1i4UAAAAAHR5S5gYSRijqySnk0OOAJpEL_9W'
RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY',
                                 '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI')

RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY',
                                  '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe')

# RECAPTCHA_TESTING = True
# RECAPTCHA_USE_SSL = False

NOCAPTCHA = True
# RECAPTCHA_PROXY = 'http://127.0.0.1:8000'


WSGI_APPLICATION = 'lamentation_wall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {}
if not os.getenv('DB_ENGINE') or os.getenv('DB_ENGINE') == 'sqlite3':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }
elif os.getenv('DB_ENGINE') == 'heroku':
    DATABASES['default'] =  dj_database_url.config(default='postgres://postgres@localhost/lamentation_wall')
    
else:
    DATABASES = {
        'default': {
            'ENGINE': os.getenv('DB_ENGINE'),
            'HOST': os.getenv('DB_HOST'),
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Parse database configuration from $DATABASE_URL

# Enable Connection Pooling (if desired)
#DATABASES['default']['ENGINE'] = 'django_postgrespool'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# compressor
COMPRESS_ENABLED=True
if 'COMPRESS_OFFLINE' in os.environ:
    COMPRESS_OFFLINE=True #this is so that compress_offline is set to true during deployment to Heroku
COMPRESS_PRECOMPILERS = (
    ('text/less','lessc {infile} {outfile}'),
)


# social auth
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GooglePlusAuth',
    'social_core.backends.google.GoogleOAuth2',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_URL = '/'
SOCIAL_AUTH_FACEBOOK_LOGIN_URL = '/'
LOGIN_URL = '/'

#SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/tetsltjauth'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('AUTH_GOOGLE_OAUTH2_SECRET')
SOCIAL_AUTH_FACEBOOK_KEY = os.getenv('AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv('AUTH_FACEBOOK_SECRET')

SOCIAL_AUTH_USER_MODEL = 'index_board.UserModel'
AUTH_USER_MODEL = 'index_board.UserModel'
