from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path("register/", Singup.as_view(), name="register"),
    path("", home, name="home"),
    path("registration/login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
