from django.urls import path

from . import views

urlpatterns = [
    path('register', views.RegisterView.as_view(), name="register"),
    path('login', views.LoginView.as_view(), name="login"),
    path('details', views.UserDetailView.as_view(), name="details"),
]