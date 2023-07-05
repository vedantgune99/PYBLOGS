from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.user_login, name="login"),
    path('signin/', views.user_signin, name="signin"),
    path('forgot_pass/', views.forgot_pass, name="forgot_pass"),
]
