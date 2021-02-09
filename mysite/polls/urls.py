from django.urls import path

from . import views

urlpatterns = [
    path('bar', views.index, name='index'),
]