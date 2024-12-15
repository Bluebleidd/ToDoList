from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home.html'),
    path('Add Board/', views.board_add, name='board_add'),
    path('<int:board_id>/', views.board, name='board'),
    path('<int:board_id>/Add Task/', views.task_add, name='task_add'),
]