from django.urls import path
from GameDB import views

app_name = 'GameDB'

urlpatterns = [
path('', views.index, name='index'),
path('login/', views.login_view, name='login'),
path('register/', views.register_view, name='register'),
]
