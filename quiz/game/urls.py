from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('quiz/', views.QuizListView.as_view(), name='quiz_list'),
    path('quiz/<int:pk>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/result/<int:pk>', views.QuizResultView.as_view(), name='quiz_result'),
]