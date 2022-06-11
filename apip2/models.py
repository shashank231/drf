from unicodedata import name
from django.db import models
from django.core.exceptions import ValidationError
from django.forms import CharField

class Department(models.Model):
    name = models.CharField(max_length=50)
    lvl = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    pay = models.IntegerField()
    dep = models.ForeignKey(Department, on_delete=models.CASCADE)   
    def __str__(self):
        return self.name                                               

class Clas(models.Model):
    grade = models.IntegerField()
    master = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    # def __int__(self):
    #     return self.grade

class Floor(models.Model):
    lvl = models.IntegerField()
    area = models.CharField(max_length=50)
    cls =  models.ForeignKey(Clas, on_delete=models.CASCADE)
    # def __int__(self):
    #     return self.lvl
