from django.conf import settings
import dj_database_url


DEBUG = False
TEMPLATE_DEBUG=False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dca1petso80la5',
        'USER': 'nrajgywlyspilh',
        'PASSWORD': 'lKZRK6HIj0GnEVcWwvg9KMefjc',
        'HOST': 'ec2-54-243-132-114.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}