from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView
)
from django.views.generic.list import MultipleObjectMixin
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


class QuizDetailView(DetailView, MultipleObjectMixin):
    model = Quiz
    context_object_name = 'quiz'
    template_name = 'game/quiz_detail.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        object_list = self.object.questions.all()
        context = super(QuizDetailView, self).get_context_data(object_list=object_list, **kwargs)
        return context
    
