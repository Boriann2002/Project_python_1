"""
WSGI-конфигурация для проекта LangTrainer.

Он предоставляет callable-объект WSGI как переменную уровня модуля с именем `application`.

Подробнее: https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE,
# указывающую на файл настроек вашего проекта.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'langtrainer.settings')

# Получаем WSGI-приложение Django
application = get_wsgi_application()