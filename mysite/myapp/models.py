from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.EmailField(max_length=50)
    Phone_no = models.CharField(max_length=11)
    def __str__(self):
        return self.first_name

class Person(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.EmailField(max_length=50)
    Phone_no = models.CharField(max_length=11)
    def __str__(self):
        return self.first_name
# Create your models here.
