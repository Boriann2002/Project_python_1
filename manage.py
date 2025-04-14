#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys


def main():
    """Основная функция для выполнения административных команд."""
    # Устанавливаем настройки Django по умолчанию
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'langtrainer.settings')

    try:
        # Пытаемся импортировать Django-модуль для управления
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Обработка ошибки, если Django не установлен
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Выполнение команды из командной строки
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()