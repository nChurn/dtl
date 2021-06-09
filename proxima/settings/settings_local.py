"""
This file generates automatically with Ansible.
Don't edit it directly. Edit the ansible/templates/settings.j2 insted.
"""

DEBUG = True

ALLOWED_HOSTS = ['proximagroup.ru', 'www.proximagroup.ru']
BASE_URL = 'http://proximagroup.ru'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'proxima_prod',
        'USER': 'proxima_prod',
        'PASSWORD': 'B5hAeMS8FP',

    },
}
