from tkinter import CASCADE
from django.db import models


# Create your models here.


class AddStudent(models.Model):
  
    fname=models.CharField(max_length=120)
    phone=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    status=models.BooleanField(default=False)

    class Meta:
        db_table="add_student"