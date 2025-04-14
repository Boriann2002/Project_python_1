"""
URL-маршруты для приложения cards.

Определяет пути для:
- Главной страницы
- Добавления уроков и карточек
- Просмотра списка карточек
- Прохождения викторины
"""
# pylint: disable=import-error
from django.urls import path
from cards import views  # Явный абсолютный импорт


urlpatterns = [
    path('', views.home, name='home'),
    path('add-lesson/', views.add_lesson, name='add_lesson'),
    path('cards/', views.CardListView.as_view(), name='card_list'),
    path('add-card/', views.add_card, name='add_card'),
    path('quiz/<int:lesson_id>/', views.quiz, name='quiz'),
]
