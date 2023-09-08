from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView

from todoapp.models import Task

class TaskList(ListView):
    model = Task
    context_object_name = "tasks"



"""
関数ベース
def taskList(request):
    return HttpResponse("<h1>Hello Django</h1>")
"""
