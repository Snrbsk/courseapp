from django.urls import path # type: ignore
from . import views


urlpatterns = [
    path('', views.index),
    path('<slug:slug>', views.detail, name= "course_details"),
    path('category/<slug:slug>', views.getCoursesByCategory,name="courses_by_category"),
]
