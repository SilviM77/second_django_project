from django.db import models
from datetime import datetime

from django.db.models.query_utils import Q

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 400)
    address = models.CharField(max_length = 300)
    zip_code = models.IntegerField()

class Grade(models.Model):
    grade = models.IntegerField()
class Certificate_type(models.Model):
    name = models.CharField(max_length = 100)
class Faculty(models.Model):
    faculty_names = models.CharField(max_length = 100, default="")
class Department(models.Model):
    department = models.CharField(max_length = 50)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
class Student(models.Model):
    fullname = models.CharField(max_length = 100)
    year_of_graduation = models.IntegerField(default = 0)
    department = models.CharField(max_length = 50)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    certificate_type = models.ForeignKey(Certificate_type, on_delete=models.CASCADE)








