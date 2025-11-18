from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=30)
    age=models.IntegerField()
    salary = models.IntegerField()
    designation = models.CharField(max_length=30)
    email = models.EmailField()