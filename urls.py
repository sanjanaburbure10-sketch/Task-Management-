from taskapp import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from taskapp.views import home, add_task, edit_task, delete_task


urlpatterns = [

    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path("add-task/", add_task, name="add_task"),

    path("edit-task/<int:task_id>/", edit_task, name="edit_task"),

    path("delete-task/<int:task_id>/", delete_task, name="delete_task"),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login"
    ),

    path(
    "logout/",
    auth_views.LogoutView.as_view(),
    name="logout"
),
path("register/", views.register, name="register"),

]