from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home),
    
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    
    path("login/register/", views.register, name='register'),
    
    path("login/register/", views.register, name='register'),
    
    path('home/login/register/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    path('home/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    path("home/register/", views.register, name='register'),
    
    path('account/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    path("register/", views.register, name='register'),
    
    path('register/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    path('comingsoon/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path("account/", views.account,  name='account'),
    
    path("categories/account/", views.account,  name='account'),

    path("search/", views.search_results, name='search_results'),

    path("categories/", views.categories),
    
    path("home/categories/", views.categories),
    
    path("comingsoon/", views.coming_soon),

    path("home/comingsoon/", views.coming_soon),

    path("about-us/", views.about_us),
    
    path("home/", views.home),

    path('chosen_game/<int:gameID>', views.chosen_game),
    
    path('account/update/', views.update_account, name='update_account'),

    path('check_login/', views.check_login)
]