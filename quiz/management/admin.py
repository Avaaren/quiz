from django.contrib import admin
from .models import (
    CurrentQuiz,
    Quiz,
    Question,
    Answer
)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'is_active']
    list_filter = ['created', 'is_active']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer_text']

@admin.register(CurrentQuiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['quiz', 'user', 'is_finished']
    # list_filter = ['created', 'is_active']