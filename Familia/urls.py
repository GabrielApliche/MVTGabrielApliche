from django.urls import path
from Familia import views

urlpatterns = [
    path("familia", views.familiares),
]