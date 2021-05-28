from django.contrib import admin
from .models import School, Student, Faculty, Certificate_type, Department, Grade

# Register your models here.

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Certificate_type)
admin.site.register(Department)
admin.site.register(Grade)