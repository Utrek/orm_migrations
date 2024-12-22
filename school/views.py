from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    students = Student.objects.all().order_by(ordering) 
    
    for s in students:
        print(f'{s.name}, {s.group}, {s.teachers}')  
    context = {'students': students}  # передаем в контекст шаблона список учеников


    return render(request, template, context)
