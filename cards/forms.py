"""
Формы для приложения cards.

Содержит формы для создания и редактирования уроков и карточек.
"""
# pylint: disable=relative-beyond-top-level
from django import forms
from .models import Lesson, Card  # Исправлен импорт


class LessonForm(forms.ModelForm):
    """
    Форма для создания и редактирования уроков.

    Attributes:
        model (Lesson): Связанная модель
        fields (list): Поля формы
        widgets (dict): Виджеты для полей формы
    """
    class Meta:
        model = Lesson
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: "Животные"'
            }),
        }


class CardForm(forms.ModelForm):
    """
    Форма для создания и редактирования карточек.

    Attributes:
        model (Card): Связанная модель
        fields (list): Поля формы
        widgets (dict): Виджеты для полей формы
    """
    class Meta:
        model = Card
        fields = ['lesson', 'word', 'translation', 'image']
        widgets = {
            'word': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: "Cat"'
            }),
            'translation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: "Кошка"'
            }),
        }
