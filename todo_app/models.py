from django.db import models

# Create your models here.
class todotask(models.Model):
    todolist=models.CharField(max_length=50)
    
