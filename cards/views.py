"""
Модуль views приложения cards.

Содержит представления для:
- Главной страницы с уроками
- Списка карточек
- Добавления уроков и карточек
- Прохождения викторины
"""
# pylint: disable=import-error
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.db.models import Count

from cards.models import Lesson, Card
from cards.forms import LessonForm, CardForm


def home(request):
    """Отображает главную страницу со списком уроков и количеством карточек."""
    lessons = Lesson.objects.annotate(card_count=Count('cards'))
    return render(request, 'cards/lessons.html', {'lessons': lessons})


class CardListView(ListView):
    """Отображает список карточек с пагинацией."""
    model = Card
    template_name = 'cards/card_list.html'
    context_object_name = 'cards'
    paginate_by = 10


def add_lesson(request):
    """Обрабатывает добавление нового урока."""
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LessonForm()
    return render(request, 'cards/add_lesson.html', {'form': form})


def add_card(request):
    """Обрабатывает добавление новой карточки."""
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('card_list')
    else:
        form = CardForm()
    return render(request, 'cards/add_card.html', {'form': form})


def quiz(request, lesson_id):
    """Обрабатывает прохождение викторины по карточкам урока."""
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    cards = lesson.cards.all()

    if request.method == 'POST':
        score = 0
        for card in cards:
            if request.POST.get(f'card_{card.id}', '').lower() == card.translation.lower():
                score += 1
        return render(request, 'cards/quiz_result.html', {
            'score': score,
            'total': len(cards),
            'percentage': (score / len(cards)) * 100 if len(cards) > 0 else 0,
            'lesson_id': lesson_id
        })

    return render(request, 'cards/quiz.html', {
        'lesson': lesson,
        'cards': cards
    })
