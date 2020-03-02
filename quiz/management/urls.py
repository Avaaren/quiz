from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    path('questions/', views.main_page, name='question_list'),
]