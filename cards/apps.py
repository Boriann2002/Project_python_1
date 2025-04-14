"""
Конфигурация приложения cards.

Определяет настройки для Django-приложения cards, включая тип автоматического поля по умолчанию.
"""

from django.apps import AppConfig


class CardsConfig(AppConfig):
    """
    Конфигурационный класс приложения cards.

    Attributes:
        name (str): Имя приложения
        default_auto_field (str): Тип автоинкрементного поля по умолчанию
    """
    name = 'cards'  # Имя приложения
    default_auto_field = 'django.db.models.BigAutoField'
