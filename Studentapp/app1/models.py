from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll_no = models.IntegerField()
    gender=models.CharField(max_length=10)
    course=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()
