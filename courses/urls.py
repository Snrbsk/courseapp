from django.urls import path # type: ignore
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('search', views.search, name= "search"),
    path('create-course', views.create_course, name= "create-course"),
    path('course-list', views.course_list, name= "course-list"),
    path('upload', views.upload, name="upload_image"),
    path('course-edit/<int:id>', views.course_edit, name= "course-edit"),
    path('course-delete/<int:id>', views.course_delete, name= "course-delete"),
    path('<slug:slug>', views.detail, name= "course_details"),
    path('category/<slug:slug>', views.getCoursesByCategory,name="courses_by_category"),
]
