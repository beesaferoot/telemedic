#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    env = os.environ.get("DJANGO_APP_ENV")
    if  env is not None:
        if 'dev' in env.lower():
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.config.dev')
        else:
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.config.production')
    else:
        raise Exception('DJANGO_APP_ENV environment variable not set')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
