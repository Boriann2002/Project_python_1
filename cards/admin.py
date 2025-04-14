"""
Административный интерфейс для приложения cards.

Регистрирует модели Lesson и Card в Django Admin, настраивает отображение и функциональность.
"""
# pylint: disable=relative-beyond-top-level
from django.contrib import admin
from .models import Lesson, Card


class CardInline(admin.TabularInline):
    """Inline-редактор для карточек внутри уроков."""

    def __init__(self, parent_model, admin_site):
        """Инициализация inline-редактора."""
        super().__init__(parent_model, admin_site)
        self.model = Card
        self.extra = 1
        self.fields = ('word', 'translation', 'image')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Lesson."""

    def get_inlines(self, request, obj=None):
        """Возвращает список inline-редакторов."""
        return [CardInline]

    def get_list_display(self, request):
        """Определяет поля для отображения в списке."""
        return ('title', 'created_at', 'card_count')

    def get_search_fields(self, request):
        """Определяет поля для поиска."""
        return ('title',)

    def card_count(self, obj):
        """Возвращает количество карточек в уроке.

        Args:
            obj: Объект Lesson

        Returns:
            int: Количество связанных карточек
        """
        return obj.cards.count()

    card_count.short_description = 'Карточек'


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Card."""

    def get_list_display(self, request):
        """Определяет поля для отображения в списке."""
        return ('word', 'translation', 'lesson', 'image_preview')

    def get_list_filter(self, request):
        """Определяет поля для фильтрации."""
        return ('lesson',)

    def get_search_fields(self, request):
        """Определяет поля для поиска."""
        return ('word', 'translation')

    def image_preview(self, obj):
        """Генерирует HTML-превью изображения.

        Args:
            obj: Объект Card

        Returns:
            str: HTML-код изображения или прочерк
        """
        if obj.image:
            return f'<img src="{obj.image.url}" width="50">'
        return "—"

    image_preview.allow_tags = True
    image_preview.short_description = 'Изображение'
