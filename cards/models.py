"""
Модуль моделей для приложения cards.

Содержит модели Lesson (Урок) и Card (Карточка) для системы изучения иностранных слов.
"""

from django.db import models
from django.core.validators import MinLengthValidator


class Lesson(models.Model):
    """
    Модель урока/тематики для группировки карточек.

    Attributes:
        title (CharField): Название урока (минимум 3 символа)
        created_at (DateTimeField): Дата создания (автоматически)
    """
    id = models.BigAutoField(primary_key=True)
    objects = None
    title = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3, "Название должно быть не короче 3 символов!")]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Card(models.Model):
    """
    Модель карточки для изучения слов.

    Attributes:
        lesson (ForeignKey): Связь с уроком
        word (CharField): Слово на иностранном языке (минимум 2 символа)
        translation (CharField): Перевод (минимум 2 символа)
        image (ImageField): Опциональное изображение
    """
    id = models.BigAutoField(primary_key=True)
    objects = None
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='cards')
    word = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2, "Слово должно быть не короче 2 символов!")]
    )
    translation = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2, "Перевод должен быть не короче 2 символов!")]
    )
    image = models.ImageField(upload_to='cards/images', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return f"{self.word} → {self.translation}"
