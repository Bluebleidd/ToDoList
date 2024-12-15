from django.shortcuts import render, redirect
from .models import Board, Task
from .forms import BoardForm, TaskForm

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_add(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home.html')
    else:
        form = BoardForm()
    return render(request, 'board_add.html', {'form': form})

def board(request, board_id):
    board = Board.objects.get(id=board_id)
    tasks = Task.objects.filter(board=board)
    return render(request, 'board.html', {'board': board, 'tasks': tasks})

def task_add(request, board_id):
    board = Board.objects.get(id=board_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.board = board
            task.save()
            return redirect('board', board_id=board.id)
    else:
        form = TaskForm()
    return render(request, 'task_add.html', {'form': form, 'board': board})