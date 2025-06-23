from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api
from decouple import config
import os

# المسار الأساسي
BASE_DIR = Path(__file__).resolve().parent.parent

# الحماية
SECRET_KEY = config('SECRET_KEY', default='django-insecure-mjol@n6t_c^_h#cn73fysw%mi&=!dg&&m7jqbluwzn97)knrp7')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="").split(",")

# التطبيقات
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # الطرف الثالث
    'cloudinary',
    'cloudinary_storage',

    # تطبيقاتك
    'store',
    'accounts',
    'dashboard',
    'cart',
]

# الوسيطات
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ ميدلوير لتقديم static في الإنتاج
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# روابط المشروع
ROOT_URLCONF = 'asssa.urls'

# القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# WSGI
WSGI_APPLICATION = 'asssa.wsgi.application'

# قاعدة البيانات
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': config('DB_ENGINE', default='django.db.backends.postgresql'),
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT', default='5432'),
        }
    }

# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# اللغة والتوقيت
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# Cloudinary
cloudinary.config(
    cloud_name=config("CLOUDINARY_CLOUD_NAME", default="duxou2ane"),
    api_key=config("CLOUDINARY_API_KEY", default="255475613753895"),
    api_secret=config("CLOUDINARY_API_SECRET", default="fcYKr7pg-BpFxolKIfNApzTGZ64"),
    secure=True
)

# التخزين السحابي للوسائط
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# الملفات الثابتة
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # ✅ عرض ملفات static في الإنتاج

# الوسائط
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# الحقل الافتراضي
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
