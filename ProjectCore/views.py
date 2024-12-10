from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Board
from .forms import TaskForm

def board_list(request):
    boards = Board.objects.all()
    can_add_board = boards.exists()

    return render(request, 'board_list.html', {'boards': boards, 'can_add_board': can_add_board})

def board_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')

        if name:
            Board.objects.create(name=name, description=description)
            return redirect('board_list')
        else:
            return render(request, 'board_add.html', {'error': 'Nazwa tablicy jest wymagana'})
    return render(request, 'board_add.html')

def board_detail(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    
    to_do_tasks = board.tasks.filter(status=Task.TO_DO)
    doing_tasks = board.tasks.filter(status=Task.DOING)
    done_tasks = board.tasks.filter(status=Task.DONE)

    return render(request, 'board_detail.html', {
        'board': board,
        'to_do_tasks': to_do_tasks,
        'doing_tasks': doing_tasks,
        'done_tasks': done_tasks,
    })

def task_add(request, board_id):
    board = Board.objects.get(id=board_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.board = board
            task.save()
            return redirect('board_detail', board_id=board.id)
    else:
        form = TaskForm()
    
    return render(request, 'task_add.html', {'form': form, 'board': board})