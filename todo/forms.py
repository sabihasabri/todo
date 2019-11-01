from django import forms
from django.forms import ModelForm
from .models import Todo
from django.utils import timezone

# from django.conf import settings


class DateInput(forms.DateInput): 
    input_type = 'date'


class TodoForm(forms.ModelForm): 
    class Meta: 
        model = Todo


        fields = [
            'text', 
            'date',
            'description', 
        ]
        widgets = {            
            'text' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'id'    : 'text', 
                    'placeholder' : 'Enter todo', 
                    'aria-lable' : 'Todo', 
                    'aria-describedby' : 'add-btn', 
                    }
                 ), 
        
        
            'date' : DateInput(
                    attrs = {
                        'class' : 'form-control', 
                        'id'     : 'date', 
                        'placeholder' : 'Select a date'
                    }
            ), 

              
            'description' : forms.Textarea( 
                    attrs = {
                        
                        "class": "form-control", 
                        "id": "description", 
                        "name": "description", 
                        "rows": 5, 
                        "cols": 20, 
                    }
            )
        
        }

# class EditForm(forms.ModelForm):
#     class Meta: 
#         model = Todo
#         fields = "__all__" 




