import os


SITE_NAME = 'AutoCustom'
SITE_DESCRIPTION = 'автозапчасти, автоателье, дейтелинг и техобслуживание в Тюмени'



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'development_secret_key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mptt',
    'ckeditor',
    'ckeditor_uploader',
    'core',
    'sliders',
    'store',
    'services',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

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
                'core.context_processors.site_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Yekaterinburg'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

MEDIA_ROOT = '%s/files/media/' % (BASE_DIR)

MEDIA_URL = '/media/'

STATIC_ROOT = '%s/files/static/' % (BASE_DIR)

STATIC_URL = '/static/'









CKEDITOR_JQUERY_URL = '/static/js/jquery-3.1.1.min.js'


CKEDITOR_UPLOAD_PATH = 'images/'

# Группировка изображений по папкам пользователей и разграниченный доступ,
# названия папок по полю username
CKEDITOR_RESTRICT_BY_USER = True

# Бэкенд для создания миниатюрок изображений
CKEDITOR_IMAGE_BACKEND = 'pillow'

# Просмотр изображений с группировкой по папкам
CKEDITOR_BROWSE_SHOW_DIRS = True

# Загрузка файлов, отличных от изображений
CKEDITOR_ALLOW_NONIMAGE_FILES = False


CKEDITOR_CONFIGS = {
        'default': {
        'resize_dir': 'both',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Source','Maximize','ShowBlocks','DocProps','Preview',],
            ['Cut','Copy','Paste','PasteText','PasteFromWord','-','Undo','Redo',],
            ['Find','Replace','-','SelectAll','-','SpellChecker',],
            ['Link','Unlink','Anchor'],
            ['Image', 'Youtube', 'Table',],
            '/',
            ['Format'],
            ['Bold','Italic','Underline'],
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
            ['NumberedList','BulletedList','-','Outdent','Indent'],
            ['Subscript','Superscript','-','Blockquote',],
            ['RemoveFormat'],
        ],
        'width': '100%',
        'format_tags': 'p;h2;h3;h4;h5;h6;pre;address;div',
        'allowedContent': False,  # разрешение на вставку скриптов
        'contentsCss': ['/sf/core/common.css', ],
        'extraPlugins': 'youtube',
    },
}
AWS_QUERYSTRING_AUTH = False
