from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logged_out.html'), name='logout'),

    path('dashboard/change-password/', auth_views.PasswordChangeView.as_view(template_name='password_change_form.html'), name='change_password'),
    path('dashboard/password-change-done/', auth_views.PasswordChangeView.as_view(template_name='password_change_done.html'), name='password_change_done'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]