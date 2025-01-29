from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Board, Task
from .forms import BoardForm, TaskForm, UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

@login_required
def board_add(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BoardForm()
    return render(request, 'board_add.html', {'form': form})

@login_required
def board(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    tasks = Task.objects.filter(board=board)
    return render(request, 'board.html', {'board': board, 'tasks': tasks})

@login_required
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

@login_required
def task_edit(request, board_id, task_id):
    board = get_object_or_404(Board, id=board_id)
    task = get_object_or_404(Task, id=task_id, board=board)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('board', board_id=board.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_edit.html', {'form': form, 'board': board, 'task': task})

@login_required
def board_edit(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BoardForm(instance=board)
    return render(request, 'board_edit.html', {'form': form, 'board': board})

@login_required
def board_delete(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    if request.method == 'POST':
        board.delete()
        return redirect('home')
    return redirect('home')

@login_required
def task_delete(request, board_id, task_id):
    board = get_object_or_404(Board, id=board_id)
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('board', board_id=board.id)
    return redirect('board', board_id=board.id)