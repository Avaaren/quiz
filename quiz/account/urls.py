from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'account'

urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(template_name='account/login.html'),
         name='login'),
    path('logout/',
         auth_views.LoginView.as_view(template_name='account/logout.html'),
         name='logout'),
    path('registration/', views.registration, name='registration'),
    path('password/change',
         auth_views.PasswordChangeView.as_view(
             template_name='account/password_change.html',
             success_url='account:password_change_done'),
         name='password_change'),
    path('password/change_done',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='account/password_change_done.html'),
         name='password_change_done'),

]
