from django.shortcuts import render, redirect, get_object_or_404
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
    # form = TodoForm(request.POST) 
    # print(request.POST['text'])
    # print(request.POST['date'])
    # print(request.POST['description'])
    # if form.is_valid():
    #     new_todo=Todo(text=request.POST['text'], date=request.POST['date'], description=request.POST['description'])
    #     new_todo.save()
    #     return redirect('todo:index')
    # return render(request, 'todo/index.html', {'form':form})

    # if request.POST.get('action') == 'post': 
    #     text = request.POST.get('title')
    #     date = request.POST.get('date')
    #     description = request.POST.get('description')
    todo_list = Todo.objects.all().order_by('id')
    form = TodoForm(request.POST) 
    response_data = {}
    if request.method == "POST": 
        text = request.POST['text']
        date = request.POST['date']
        description = request.POST['description']
        if form.is_valid(): 
            instance = form.save(commit=True)
            # return redirect('todo:index')
    

        response_data['text'] = text
        response_data['date'] = date
        response_data['description'] = description
        Todo.objects.create(
            text = text, 
            date = date, 
            description = description, 
        )
        return JsonResponse(response_data)
        
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

        # Todo.objects.create(
        #     text=text, 
        #     date=date, 
        #     description=description, 
        # )


        form = TodoForm(request.POST, instance=instance)
        if form.is_valid(): 
            instance = form.save(commit=True)
            return redirect('todo:index')

    return render(request, 'todo/edit.html', {'form':form})
    return HttpResponse('')