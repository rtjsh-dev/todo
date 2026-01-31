from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def addTask(request):
    HttpResponse("The form is submitted.")