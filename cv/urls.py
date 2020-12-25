from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('simple', views.simple, name="simple"),
    path('data', views.data, name="data"),
    path('fx', views.fx, name="fx"),
    path('patterns', views.patterns, name="patterns"),
]
