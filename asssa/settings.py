from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api

# ✅ المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ إعدادات الحماية
SECRET_KEY = 'django-insecure-mjol@n6t_c^_h#cn73fysw%mi&=!dg&&m7jqbluwzn97)knrp7'
DEBUG = True
ALLOWED_HOSTS = []

# ✅ التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات الطرف الثالث
    'cloudinary',
    'cloudinary_storage',

    # تطبيقات المشروع
    'store',
    'accounts',
    'dashboard',
]

# ✅ الوسيطات
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ✅ روابط المشروع
ROOT_URLCONF = 'asssa.urls'

# ✅ إعداد القوالب
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

# ✅ تطبيق WSGI
WSGI_APPLICATION = 'asssa.wsgi.application'

# ✅ قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ✅ التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ✅ اللغة والتوقيت
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# ✅ إعدادات Cloudinary
cloudinary.config( 
  cloud_name = "duxou2ane",
  api_key = "255475613753895",
  api_secret = "fcYKr7pg-BpFxolKIfNApzTGZ64",
  secure = True
)

# ✅ التخزين السحابي للوسائط (صور المنتجات مثلاً)
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# ✅ الملفات الثابتة (CSS/JS)
STATIC_URL = 'static/'

# ✅ إعدادات الوسائط (لن تُستخدم مع Cloudinary لكن نتركها احتياطًا)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ✅ الحقل الافتراضي للموديلات
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
