from django.urls import path # type: ignore
from . import views


urlpatterns = [
    path('', views.index),
    path('<course_name>', views.detail),
    path('category/<int:category_id>', views.getCoursesByCategoryId),
    path('category/<str:category_name>', views.getCoursesByCategory,name="courses_by_category"),
]
