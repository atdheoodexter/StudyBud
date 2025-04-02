from __future__ import absolute_import, unicode_literals
import os
from .base import *  # noqa

# Load environment variables
env = os.environ.copy()

# SECURITY SETTINGS
DEBUG = False  # Always False in production
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Ensure that only allowed hosts are permitted
ALLOWED_HOSTS = env.get('ALLOWED_HOSTS', 'yourdomain.com,www.yourdomain.com').split(',')

# Use environment variable for the secret key
SECRET_KEY = env.get('SECRET_KEY')

# DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.get('DB_NAME', 'postgres'),
        'USER': env.get('DB_USER', 'postgres'),
        'PASSWORD': env.get('DB_PASSWORD', 'password'),
        'HOST': env.get('DB_HOST', 'db'),  # 'db' if using Docker, or an actual hostname/IP
        'PORT': env.get('DB_PORT', '5432'),
    }
}

# STATIC & MEDIA FILES (for production)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

# ENABLE COMPRESSION (for CSS/JS performance optimization)
COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CssMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'

# LOGGING CONFIGURATION (Production Logging)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': env.get('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

# EMAIL CONFIGURATION (For sending emails)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(env.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env.get('EMAIL_HOST_PASSWORD')

# RECAPTCHA CONFIGURATION (Google Recaptcha)
RECAPTCHA_PRIVATE_KEY = env.get('RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_PUBLIC_KEY = env.get('RECAPTCHA_PUBLIC_KEY')

# IMPORT LOCAL SETTINGS (if any)
try:
    from .local import *
except ImportError:
    pass
