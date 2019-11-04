from django.urls import path 
from . import views



app_name = 'todo'

urlpatterns = [
    path('TODO', views.index, name='index'),
    path ('add/', views.addTodo, name='add'),
    path ('complete/<todo_id>/', views.completeTodo, name='complete'),
    path ('edit/<todo_id>/', views.edit , name='edit'), 
    path ('delete/', views.deleteCompleted, name='delete'),
    path ('deleteAll/', views.deleteAll, name='deleteAll'),
    path('todolist/', views.Todolist, name='todolist'), 
    
]
