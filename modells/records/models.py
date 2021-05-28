from django.db import models
from datetime import datetime

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 400)
    address = models.CharField(max_length = 300)
    zip_code = models.IntegerField()

class Student(models.Model):
    fullname = models.CharField(max_length = 100)
    year_of_graduation = models.IntegerField()
    department = models.CharField(max_length = 50)
    grade = models.IntegerField()
    certificate_type = models.CharField(max_length = 100)

class Certificate_type(models.Model):
    name = models.CharField(max_length = 100)

class Faculty(models.Model):
    faculty_names = models.CharField(max_length = 100)

class Department(models.Model):
    department = models.CharField(max_length = 50)
    faculty_names = models.CharField(max_length = 100)

class Grade(models.Model):
    grade = models.IntegerField()
