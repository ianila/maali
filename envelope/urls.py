from django.urls import path

from .import views

urlpatterns = [
    path('', views.EnvelopeList.as_view()),
    path('<int:id>', views.EnvelopeDetailView.as_view()),
]