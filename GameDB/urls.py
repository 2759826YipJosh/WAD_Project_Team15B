from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home),
    
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    
    path("login/register/", views.register, name='register'),
    
    path("register/", views.register, name='register'),
    
    path('register/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    path('account/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path("account/", views.account,  name='account'),

    path("search/", views.search),

    path("categories/", views.categories),

    path("comingsoon/", views.coming_soon),

    path("about-us/", views.about_us),
]