from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    #model - Database structure
    #views - Application Logic
    #Template - HTML User Interface
    #URL - connects the browser request to views