from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('edit_profile/<int:user_id>', views.edit_profile, name="edit_profile"),
    path('del_prof_img/<int:user_id>',
         views.del_profile_img, name="del_profile_img"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('signin/', views.user_signin, name="signin"),

    # Password Reset Points...
    path('reset_password/',  auth_views.PasswordResetView.as_view(template_name='reset_password.html'),
         name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_email_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset_confirm.html"),
         name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_finished.html"),
         name="password_reset_complete"),
]
