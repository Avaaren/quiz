from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

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

    path('password_change/',
         auth_views.PasswordChangeView.as_view(
             template_name='account/password_change.html',
             success_url=reverse_lazy('account:password_change_done')),
         name='password_change'),

    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='account/password_change_done.html'),
         name='password_change_done'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='account/password_reset.html',
             email_template_name='account/password_reset_email.html',
             success_url=reverse_lazy('account:password_reset_done')),
         name='password_reset'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
            template_name='account/password_reset_done.html'  
         ),
         name='password_reset_done'),

    path('password_reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='account/password_reset_confirm.html',
             success_url=reverse_lazy('account:password_reset_complete')),
         name='password_reset_confirm'),

    path('password_reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='account/password_reset_complete.html'),
         name='password_reset_complete')
]
