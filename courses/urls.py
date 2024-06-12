from django.urls import path
from . views import *


urlpatterns = [
    path('', views.home),
    path('home/', views.home),
]
