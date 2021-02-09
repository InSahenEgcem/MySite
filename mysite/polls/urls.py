from django.urls import path

from . import views

urlpatterns = [
    path('bar', views.foo, name='index'),
    path('smashted', views.bar, name='index'),
]