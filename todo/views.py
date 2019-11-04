from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_POST
from .models import Todo
from django.http import JsonResponse
from .forms import TodoForm
from django.forms import ModelForm
from django.views.generic.edit import UpdateView


def index(request): 
    todo_list = Todo.objects.all().order_by('id')
    form = TodoForm()
    print(todo_list)

    context = {'todo_list'  : todo_list, 'form' : form}
    return render(request, 'todo/index.html', context)

# @require_POST
def addTodo(request): 
    form = TodoForm(request.POST) 
    if form.is_valid():
        new_todo=Todo(text=request.POST['text'], date=request.POST['date'], description=request.POST['description'])
        new_todo.save()
        return redirect('todo:index')
    return render(request, 'todo/index.html', {'form':form})

    

def completeTodo(request, todo_id): 
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = not todo.complete
    todo.save() 
    return redirect('todo:index')


def deleteCompleted(request): 
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('todo:index')

def deleteAll(request): 
    Todo.objects.all().delete()

    return redirect('todo:index')

           

def edit(request, todo_id):

    instance = get_object_or_404(Todo, id=todo_id)
    form = TodoForm(instance=instance)
    if request.method == "POST": 


        text = request.POST['text']
        date = request.POST['date']
        description = request.POST['description']


        form = TodoForm(request.POST, instance=instance)
        if form.is_valid(): 
            instance = form.save(commit=True)
            return redirect('todo:index')

    return render(request, 'todo/edit.html', {'form':form})
    

def Todolist(request): 
    todo_list = Todo.objects.all().order_by('id')
    form = TodoForm()
    print(todo_list)

    context = {'todo_list'  : todo_list, 'form' : form}
    return render(request, 'todo/list.html', context)


# def addTodo(request): 
#     form = TodoForm()
#     if request == 'POST':
        
