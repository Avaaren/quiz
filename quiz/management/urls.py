from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    path('quiz/', views.QuizListView.as_view(), name='quiz_list'),
    path('quiz/<int:pk>', views.QuizDetailView.as_view(), name='quiz_detail'),
]