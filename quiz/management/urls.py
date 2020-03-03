from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    path('quiz/', views.QuizListView.as_view(), name='quiz_list'),
    path('quiz/<int:pk>', views.QuizDetailView.as_view(), name='quiz_detail'),
    # path('question/create/',
    #      views.QuestionCreateView.as_view(),
    #      name='question_create'),
    path('question/', views.QuestionListView.as_view(), name='question_list'),
    path('question/<int:pk>',
         views.QuestionDetailView.as_view(),
         name='question_detail'),
    path('question/edit/<int:pk>/',
         views.QuestionEditView.as_view(),
         name='question_edit'),
]
