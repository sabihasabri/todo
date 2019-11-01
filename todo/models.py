from django.db import models
from django.utils import timezone




class Todo(models.Model): 
    text = models.TextField(max_length=500)
    complete = models.BooleanField(default=False) 
    date = models.DateField(default=timezone.now)
    description = models.TextField(max_length=500, blank=True) 
    
    
   
    def __str__(self):
        return self.text
    
    # def get_absolute_url(self):
    #     return reverse('edit', kwargs={'id': self.id})
