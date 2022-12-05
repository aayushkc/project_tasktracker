from datetime import datetime
import email
from tkinter import N
from django.db import models

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=100)
    task_desc = models.TextField(max_length=200)
    task_category = models.CharField(max_length=100)
    task_assign_date = models.DateField(null= True, blank=True)
    task_end_date = models.DateField(null= True, blank=True)
    task_assign_to = models.EmailField(default=None, unique=True)
    task_assigned_by = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField( null = True, blank=True)
    task_file = models.FileField()
    def __str__(self):
        return self.task_title
        
    class Meta:
        db_table = 'tbl_task'
class AppUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'tbl_user'