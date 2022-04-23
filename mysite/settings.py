"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import django_heroku
import dj_database_url as DATABASE_URL
import sys


from pathlib import Path


SITE_ID = 2
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nc+9%$spfhk)0c7^c%jq#f&f7npk@%i!srbn10$4-0olj-#f)1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '0.0.0.0',
    'uva-cs3240s22a08-word-of-mouth.herokuapp.com',
    'uva-cs3240s22a08-womt.herokuapp.com',
    'testserver',
    
    'womt-image-api-test.herokuapp.com',
]


# Application definition

INSTALLED_APPS = [
    # Styling
    'bootstrap5',

    # Default Django items
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Image storage
    'storages',
    
    #OAUth stuff
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",

    # Sub apps
    "home",
    "recipes",
    "users",
    "review",
]

# Use FOR OAuth
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
   }
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {}
def set_default_database():
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3'
    }

if 'test' in sys.argv:
    set_default_database()
else:
  try:
    DATABASES['default'] = DATABASE_URL.parse(os.environ['DATABASE_URL'], conn_max_age=600)
  except KeyError:
    set_default_database()

# DATABASES = {}
# DATABASES['default'].update(DATABASE_URL.config(conn_max_age=600))

# Drop SSL mode for SQLite
# options = DATABASES['default'].get('OPTIONS', {})
# options.pop('sslmode', None)

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

AUTHENTICATION_BACKENDS = (
   "django.contrib.auth.backends.ModelBackend",
   "allauth.account.auth_backends.AuthenticationBackend",
)


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')


AWS_ACCESS_KEY_ID           = os.environ["AWS_ACCESS_KEY_ID"]                   if "AWS_ACCESS_KEY_ID"          in os.environ else ""
AWS_SECRET_ACCESS_KEY       = os.environ["AWS_SECRET_ACCESS_KEY"]               if "AWS_SECRET_ACCESS_KEY"      in os.environ else ""
AWS_STORAGE_BUCKET_NAME     = os.environ["AWS_STORAGE_BUCKET_NAME"]             if "AWS_STORAGE_BUCKET_NAME"    in os.environ else ""
AWS_S3_CUSTOM_DOMAIN        = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_FILE_OVERWRITE       = False
AWS_DEFAULT_ACL             = None

AWS_S3_OBJECT_PARAMETERS    = {
    'CacheControl': 'max-age=86400',
}

AWS_LOCATION                = 'static'
STATICFILES_STORAGE         = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL                  = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

DEFAULT_FILE_STORAGE        = 'mysite.storage_backends.MediaStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

try:
    if 'HEROKU' in os.environ:
        import django_heroku
        django_heroku.settings(locals())
        SITE_ID = 2
except ImportError:
    found = False
