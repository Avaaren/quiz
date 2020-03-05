from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from management.models import (
    Quiz,
    Question,
    Answer
)


def main_page(request):
    return render(request, 'game/main_page.html', {})


class QuizListView(ListView, LoginRequiredMixin):
    model = Quiz
    context_object_name = 'quiz_list'
    template_name = 'game/quiz_list.html'


class QuizDetailView(DetailView):
    model = Quiz
    context_object_name = 'quiz'
    template_name = 'game/quiz_detail.html'

