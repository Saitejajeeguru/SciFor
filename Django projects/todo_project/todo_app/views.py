from django.shortcuts import render, redirect
from .models import TodoItem

def index(request):
    todo_list = TodoItem.objects.all()
    return render(request, 'todo_app/index.html', {'todo_list': todo_list})

def add_todo(request):
    if request.method == 'POST':
        text = request.POST.get('todoUserInput', '')
        if text:
            TodoItem.objects.create(text=text)
    return redirect('index')

def delete_todo(request, todo_id):
    TodoItem.objects.filter(pk=todo_id).delete()
    return redirect('index')

def update_todo_status(request, todo_id):
    todo_item = TodoItem.objects.get(pk=todo_id)
    todo_item.is_checked = not todo_item.is_checked
    todo_item.save()
    return redirect('index')
