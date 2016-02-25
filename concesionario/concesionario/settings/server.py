from django.conf import settings
import dj_database_url


DEBUG = False
TEMPLATE_DEBUG=False

ALLOWED_HOSTS = ['*']

DATABASES = settings.DATABASES
DATABASES = {'default': dj_database_url.config()}

