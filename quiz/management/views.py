from django.shortcuts import (
    get_object_or_404,
    redirect
)

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from django.views.generic.base import (
    View,
    TemplateResponseMixin,
)

from .models import (
    Quiz,
    Question
)
from .forms import QuestionFormSet


class QuizListView(ListView):
    model = Quiz
    ordering = ['-created']
    template_name = 'management/quiz_list.html'
    context_object_name = 'quiz_list'


class QuizDetailView(DetailView):
    model = Quiz
    context_object_name = 'quiz'
    template_name = 'management/quiz_detail.html'


class QuestionEditView(TemplateResponseMixin, View):
    template_name = 'management/question_edit.html'
    question = None

    def get_formset(self, data=None):
        return QuestionFormSet(instance=self.question,
                               data=data)

    def dispatch(self, request, *args, **kwargs):
        self.question = get_object_or_404(Question,
                                          pk=self.kwargs['pk'])
        return super(QuestionEditView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'question': self.question,
                                        'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('management:question_list')
        return self.render_to_response({'course': self.course,
                                        'formset': formset})


class QuestionListView(ListView):
    model = Question
    # ordering = ['-question_text']
    template_name = 'management/question_list.html'
    context_object_name = 'question_list'


class QuestionDetailView(DetailView):
    model = Question
    context_object_name = 'question'
    template_name = 'management/question_detail.html'