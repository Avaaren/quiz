from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView,
)

from .models import (
    Quiz,
)


class QuizListView(ListView):
    model = Quiz
    ordering = ['-created']
    template_name = 'management/quiz_list.html'
    context_object_name = 'quiz_list'


class QuizDetailView(DetailView):
    model = Quiz
    context_object_name = 'quiz'
    template_name = 'management/quiz_detail.html'
    
