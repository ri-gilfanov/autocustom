from .common import *

INTERNAL_IPS = ['localhost', '127.0.0.1']  # для debug_toolbar


INSTALLED_APPS.extend([
    'debug_toolbar',
])


MIDDLEWARE.extend([
    'debug_toolbar.middleware.DebugToolbarMiddleware',
])
