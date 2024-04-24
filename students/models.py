from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default="") 
    age = models.IntegerField()
