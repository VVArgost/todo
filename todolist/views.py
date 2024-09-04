from django.shortcuts import render, redirect

from .models import Todolist
from .forms import TodoListForm
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    todo_items = Todolist.objects.all().order_by('id')
    form = TodoListForm()
    context = {'todo_items': todo_items, 'form': form}
    return render(request, 'todolist/index.html', context)

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)

    if form.is_valid():
        hidden_text = request.POST.get('hidden_text', '')
        if hidden_text:
            new_todo = Todolist(text=hidden_text, is_invisible=True)
        else:
            new_todo = Todolist(text=request.POST['text'], is_invisible=False)
        new_todo.save()

    return redirect('index')

def completedTodo(request, todo_id):  
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()

    return redirect('index')


def deleteCompleted(request):
    Todolist.objects.filter(completed__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todolist.objects.all().delete()

    return redirect('index')




