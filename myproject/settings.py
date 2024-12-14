from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key-here'  # Replace with a secure key for production

DEBUG = True  # Set to False in production

ALLOWED_HOSTS = ['*']  # Change to your domain in production

AUTH_USER_MODEL = 'myapp.User'

# PayPal and Finnhub configuration
PAYPAL_MODE = 'sandbox'  # or 'live' for production
PAYPAL_CLIENT_ID = 'AUochiV1uTo7obVaBbCynrloiRcEpocs3Tb3noA_F7qYlwYpUAVcSpVEVjVu2YaIYjDWrG5dnBZEwI8I'
PAYPAL_CLIENT_SECRET = 'EPJUvKhzsMZrvVzC1lH0TtWTnzxBN1IViY0uy7Ov0dg2enTr0I_E-qQn8gPAD6yYoAq4uXccD78vuifB'
FINNHUB_API_KEY = 'csdanvhr01qi0n6en14gcsdanvhr01qi0n6en150'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'rest_framework',
    'rest_framework.authtoken', 
    'django_filters',
    'corsheaders',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        # Add TokenAuthentication if needed
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Optional: You can use this to disable CSRF middleware for API routes in Django
CSRF_COOKIE_HTTPONLY = False

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

RAZORPAY_KEY_ID = 'rzp_test_yourKeyHere'  # Replace with your Razorpay key
RAZORPAY_KEY_SECRET = 'yourKeySecretHere'  # Replace with your Razorpay secret

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'myproject.urls'
WSGI_APPLICATION = 'myproject.wsgi.application'

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Set static root directory
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Application-specific static files
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

if os.getenv("DOCKERIZED") == "true":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB', 'your_default_dbname'),
            'USER': os.getenv('POSTGRES_USER', 'your_default_user'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'your_default_password'),
            'HOST': os.getenv('POSTGRES_HOST', 'db'),  # Use 'db' when in Docker
            'PORT': '5432',
        }
    }
else:
    # Local development (can use SQLite or PostgreSQL on localhost)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Cairo'
USE_I18N = True
USE_TZ = True

LOGOUT_REDIRECT_URL = '/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
