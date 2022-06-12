from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # this is the main page that is given if the person asks for nothing
    path("school", views.school, name="school")
]