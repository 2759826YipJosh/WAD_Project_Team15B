from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),

    path("login/", views.user_login),

    path("register/", views.register),

    path("login/register/", views.register),

    path("account/", views.account),

    path("search/", views.search),

    path("categories/", views.categories),

    path("comingsoon/", views.coming_soon),

    path("about-us/", views.about_us),
]