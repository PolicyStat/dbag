#!/usr/bin/env python

import sys

from django.conf import settings
from django.core.management import execute_from_command_line

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='sqlite3',
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            },
        },
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.admin',
            'django.contrib.sessions',
            'django.contrib.contenttypes',
            'django.contrib.messages',

            'dbag',
        ],
        ROOT_URLCONF='dbag.urls',
        DEBUG=False,
        SECRET_KEY='dummy-key-for-testing',
        TEMPLATE_STRING_IF_INVALID="INVALID_TEMPLATE_VARIABLE",
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'debug': True,
                'string_if_invalid': 'INVALID_TEMPLATE_VARIABLE',
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.request',
                    'django.contrib.messages.context_processors.messages',
                ]
            }
        }],
        MIDDLEWARE=[
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ],
        SILENCED_SYSTEM_CHECKS=[
            'admin.E402',
        ],
    )


def runtests():
    argv = sys.argv[:1] + ['test', 'dbag', '--traceback'] + sys.argv[1:]  # noqa
    execute_from_command_line(argv)


if __name__ == '__main__':
    runtests()
