from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('AddBoard/', views.board_add, name='board_add'),
    path('<int:board_id>/', views.board, name='board'),
    path('<int:board_id>/AddTask/', views.task_add, name='task_add'),

    path('register/', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]