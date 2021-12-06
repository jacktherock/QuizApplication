from django.urls import path
from .views import create, home

urlpatterns = [
    path('', home, name="home"),
    path('create/', create, name="create"),
]