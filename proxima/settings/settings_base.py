import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_URL = 'http://localhost:8000'
SECRET_KEY = 'gE0JcU9eoP4dWzThug7JojJmiMEf4n5T37EarVhPohwi8fiGL8'

WSGI_APPLICATION = 'proxima.wsgi.application'
ADMIN_SITE_HEADER = 'Django Admin'
AUTH_USER_MODEL = 'users.User'
ROOT_URLCONF = 'proxima.urls'
DEBUG = True

USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True

ADMINS = [
    # ('Max Poletaev', 'max.poletaev@gmail.com'),
]

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',

    'proxima',
    'users',
    'pages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'static/svg')],
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


# Databases
# https://docs.djangoproxima.com/en/1.11/ref/databases/

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

SUMMERNOTE_CONFIG = {
    'toolbar': [
        ['font', ['italic','clear']],
    ],
}

# Internationalization
# https://docs.djangoproxima.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)

MODELTRANSLATION_LANGUAGES = ('en', 'ru')

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'ru'
MODELTRANSLATION_FALLBACK_LANGUAGES = ('ru', 'en', )
MODELTRANSLATION_DEBUG = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproxima.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'public', 'media')

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

# Sessions
# https://docs.djangoproxima.com/en/1.11/topics/http/sessions/

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'


# Email
# https://docs.djangoproxima.com/en/1.11/topics/email/

# Email settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_HOST_USER = 'Redis CA'
EMAIL_HOST_PASSWORD = '6r0MGPodpMQJ_Rl4dXuDqg'
DEFAULT_FROM_EMAIL = 'noreply@redis.tv'
EMAIL_PORT = 587
