from django.urls import path # type: ignore
from . import views


urlpatterns = [
    path('login', views.user_login, name="user_login"),
    path('register', views.user_register, name="user_register"),
    path('logout', views.user_logout, name="user_logout"),
    path('change_password', views.change_password, name="change_password"),

]
