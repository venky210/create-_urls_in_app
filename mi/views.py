from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def arjun(request):
    return render(request,'arjun.html')

def Bumrah(request):
    return HttpResponse("<h1>one of the bowler</h1>")
