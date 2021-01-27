"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

env = os.environ.get("DJANGO_APP_ENV")
if env is not None:
    if 'dev' in env.lower():
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.config.dev')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.config.production')
else:
    raise Exception('DJANGO_APP_ENV environment variable not set')

application = get_wsgi_application()
