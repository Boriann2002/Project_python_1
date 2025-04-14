import os
from pathlib import Path

# Базовые настройки
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'ваш-secret-key-сгенерируйте-новый'
DEBUG = True  # В продакшене установить False
ALLOWED_HOSTS = ['*']  # Для разработки. В продакшене указать домен.

# Приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cards.apps.CardsConfig',  # приложение
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLs и шаблоны
ROOT_URLCONF = 'langtrainer.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Глобальные шаблоны
        'APP_DIRS': True,  # Искать шаблоны в папках приложений
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

# База данных (SQLite по умолчанию)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Валидация паролей (для полного выхода)
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

# Язык и время
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# Статические файлы (CSS, JS, изображения)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Папка с вашими CSS/JS

# Медиафайлы (загруженные пользователями)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Папка для изображений карточек

# Дефолтный перенаправление после входа
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Для продакшена (если нужно)
if not DEBUG:
    STATIC_ROOT = BASE_DIR / 'staticfiles'  # Для collectstatic
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'