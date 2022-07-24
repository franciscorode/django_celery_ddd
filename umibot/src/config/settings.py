"""
Django settings for umibot project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import logging
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-9-6dwium-56%2iqp$tf^k)*fzn)*&bh3r+d&ne%sulw#bfd%-j"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS: list[str] = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_yasg",
    "rest_framework.authtoken",
    "src.shared.infrastructure",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = "src.api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("PROJECT_NAME"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_ROOT = "/static"
STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# API
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.JSONParser",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "EXCEPTION_HANDLER": "src.api.exception_handler.custom_exception_handler",
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

CORS_ORIGIN_ALLOW_ALL = True

# LOGGING
APP_LOG_LEVEL = "DEBUG"

LOGGING_ROOT_DIR = os.getenv("LOGGING_ROOT_DIR", os.path.join(BASE_DIR, "logs"))
LOGGING_FILE_PATH = os.path.join(LOGGING_ROOT_DIR, "umibot.log")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    # Formatters specify the layout of log records in the final output.
    "formatters": {
        "simple": {
            "format": (
                "[%(asctime)s.%(msecs)03d] %(levelname)s (%(name)s) "
                "[%(filename)s::%(funcName)s:%(lineno)d] %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "verbose": {
            "format": "[%(asctime)s.%(msecs)03d]["
            + "][%(process)d|%(thread)d] %(levelname)s (%(name)s) "
            "[%(filename)s::%(funcName)s:%(lineno)d] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    # Handlers send the log records (created by loggers) to the appropriate destination.
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.WatchedFileHandler",
            "filename": LOGGING_FILE_PATH,
            "formatter": "simple",
        },
    },
    # Loggers expose the interface that application code directly uses.
    "loggers": {
        "django.template": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "django.db": {
            "handlers": ["console", "file"],
            "level": "WARNING",
            "propagate": True,
        },
        "django.security": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "py.warnings": {
            "handlers": [
                "console",
            ],
        },
        "django": {
            "handlers": ["console", "file"],
            "level": APP_LOG_LEVEL,
            "propagate": True,
        },
        "src": {
            "handlers": ["console", "file"],
            "level": APP_LOG_LEVEL,
            "propagate": False,
        },
        "rest_api": {
            "handlers": ["console", "file"],
            "level": APP_LOG_LEVEL,
            "propagate": True,
        },
        "django.utils.autoreload": {
            "level": "INFO",
        },
    },
}

if "test" in sys.argv:
    logging.disable(logging.CRITICAL)

# Dev tools
if DEBUG and "test" not in sys.argv:
    from debug_toolbar.settings import PANELS_DEFAULTS

    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
    DEBUG_TOOLBAR_PANELS = PANELS_DEFAULTS
    INTERNAL_IPS = ["127.0.0.1"]


AUTH_USER_MODEL = "infrastructure.SqlUser"
