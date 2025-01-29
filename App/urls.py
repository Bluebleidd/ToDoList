from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('AddBoard/', views.board_add, name='board_add'),
    path('<int:board_id>/', views.board, name='board'),
    path('board/edit/<int:board_id>/', views.board_edit, name='board_edit'),
    path('board/delete/<int:board_id>/', views.board_delete, name='board_delete'),

    path('board/<int:board_id>/AddTask/', views.task_add, name='task_add'),
    path('board/<int:board_id>/task/<int:task_id>/edit/', views.task_edit, name='task_edit'),
    path('board/<int:board_id>/task/<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('board/<int:board_id>/delete-done/', views.delete_done_tasks, name='delete_done_tasks'),

    path('register/', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]