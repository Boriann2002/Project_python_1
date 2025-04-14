"""
Модуль тестирования для приложения cards.

Содержит unit-тесты для моделей, представлений и форм.
"""
# pylint: disable=relative-beyond-top-level
import os
from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from .models import Lesson, Card
from .forms import CardForm


class LessonModelTest(TestCase):
    """Тестирование модели Lesson."""

    @classmethod
    def setUpTestData(cls):
        """Создание тестовых данных."""
        cls.lesson = Lesson.objects.create(title="Животные")

    def test_title_label(self):
        """Проверка метки поля title."""
        lesson = Lesson.objects.get(id=1)
        field_label = lesson._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        """Проверка максимальной длины поля title."""
        lesson = Lesson.objects.get(id=1)
        max_length = lesson._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_title(self):
        """Проверка строкового представления модели."""
        lesson = Lesson.objects.get(id=1)
        expected_object_name = lesson.title
        self.assertEqual(str(lesson), expected_object_name)


class CardModelTest(TestCase):
    """Тестирование модели Card."""

    @classmethod
    def setUpTestData(cls):
        """Создание тестовых данных."""
        lesson = Lesson.objects.create(title="Тест урок")
        cls.card = Card.objects.create(
            lesson=lesson,
            word="Cat",
            translation="Кошка"
        )

    def test_word_validation(self):
        """Проверка валидации минимальной длины слова."""
        card = Card.objects.get(id=1)
        card.word = "A"  # Меньше минимальной длины
        with self.assertRaises(ValidationError):
            card.full_clean()


class ViewsTest(TestCase):
    """Тестирование представлений."""

    def setUp(self):
        """Инициализация тестовых данных."""
        self.client = Client()
        self.lesson = Lesson.objects.create(title="Тест урок")
        self.card = Card.objects.create(
            lesson=self.lesson,
            word="Dog",
            translation="Собака"
        )

    def test_home_view_status_code(self):
        """Проверка доступности главной страницы."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_card_list_view(self):
        """Проверка отображения списка карточек."""
        response = self.client.get(reverse('card_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dog")
        self.assertTemplateUsed(response, 'card_list.html')

    def test_add_card_view(self):
        """Проверка добавления новой карточки."""
        response = self.client.post(reverse('add_card'), {
            'lesson': self.lesson.id,
            'word': "Bird",
            'translation': "Птица"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Card.objects.filter(word="Bird").exists())


class FormTests(TestCase):
    """Тестирование форм."""

    def setUp(self):
        """Инициализация тестовых данных."""
        self.lesson = Lesson.objects.create(title="Тест")

    def test_card_form_valid_data(self):
        """Проверка формы с валидными данными."""
        form_data = {
            'lesson': self.lesson.id,
            'word': "Fish",
            'translation': "Рыба"
        }
        form = CardForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_card_form_invalid_data(self):
        """Проверка формы с невалидными данными."""
        form_data = {
            'word': "",  # Пустое поле
            'translation': "Рыба"
        }
        form = CardForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('word', form.errors)


class ImageUploadTest(TestCase):
    """Тестирование загрузки изображений."""

    def setUp(self):
        """Инициализация тестовых данных."""
        self.lesson = Lesson.objects.create(title="Тест урок")
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x00\x01\x02\x03',
            content_type='image/jpeg'
        )

    def tearDown(self):
        """Очистка тестовых файлов."""
        for card in Card.objects.all():
            if card.image and os.path.exists(card.image.path):
                os.remove(card.image.path)

    def test_card_with_image(self):
        """Проверка загрузки изображения для карточки."""
        card = Card.objects.create(
            lesson=self.lesson,
            word="Tiger",
            translation="Тигр",
            image=self.test_image
        )
        self.assertTrue(card.image.name.endswith('.jpg'))
