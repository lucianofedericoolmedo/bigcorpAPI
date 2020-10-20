from project.base_settings import *
import sys
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!zxmc^48#eli@!494w9^#56#nf*xp7s&#zu+n)82z&yxsnwnu#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'testserver']


WSGI_APPLICATION = 'project.wsgi_sqlite.application'

#INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

"""
REQUERED FOR https://vxlabs.com/2015/12/08/gunicorn-as-your-django-development-server/
SETUP GUNICORN + DJ-STATIC

ALSO CHECK: https://github.com/heroku-python/dj-static

TODO: WHITENOISE INTEGRATION
"""

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

MP_URLS = {
        'success': 'http://localhost:3000/donacion',
        'pending': 'http://localhost:3000/donacion',
        'failure': 'http://localhost:3000/donacion'
}
