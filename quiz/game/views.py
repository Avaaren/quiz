from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import json
from django.views.generic import (
    ListView,
    DetailView
)
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from management.models import (
    CurrentQuiz,
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


# class QuizDetailView(DetailView, MultipleObjectMixin):
#     model = Quiz
#     context_object_name = 'quiz'
#     template_name = 'game/quiz_detail.html'
#     paginate_by = 1

#     def get_context_data(self, **kwargs):
#         object_list = self.object.questions.all()
#         context = super(QuizDetailView, self).get_context_data(object_list=object_list, **kwargs)
#         return context


def quiz_detail(request, pk):
    quiz_object = get_object_or_404(Quiz, pk=pk)
    current_quiz_object = CurrentQuiz.objects.get_or_create(
        quiz=quiz_object,
        user=request.user,
        is_finished=False
    )[0]
    question_queryset = current_quiz_object.quiz.questions.all()

    if request.method == 'POST':
        response_data = {}
        # мы отправляем сюда ажакс пост запрос и туда кидаем атрибут экшн
        if request.POST.get('action') == 'post':
            # Получаем айди ответа переданный в ажакс и смотрим правильный ли ответ, если да, то...
            current_question_id = current_quiz_object.questions_passed + 1
            chosen_answer_id = request.POST.get('chosen_answer_id', None)
            answer = current_quiz_object.quiz.questions.get(
                pk=current_question_id).answers.get(pk=chosen_answer_id)

            if answer.is_correct:
                current_quiz_object.questions_passed += 1
                current_quiz_object.total_score += 1
                response_data['is_correct'] = True
                response_data['current_question_id'] = current_question_id+1
                current_quiz_object.save()
            else:
                current_quiz_object.questions_passed += 1
                response_data['is_correct'] = False
                response_data['current_question_id'] = current_question_id + 1
                current_quiz_object.save()
            return JsonResponse(response_data)

    return render(request, 'game/quiz_detail.html', {
        'current_quiz_object': current_quiz_object,
        'question_queryset': question_queryset,
    })

