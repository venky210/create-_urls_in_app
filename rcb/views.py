from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return render(request,'virat.html')

def maxwell(request):
    return HttpResponse('<h1><marquee>All Rounder</marquee></h1>')
