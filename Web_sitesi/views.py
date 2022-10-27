from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.

def intro(request):
     return render(request,"intro.html")

def about(request):
     return render(request,"about.html")

def work(request):
     return render(request,"work.html")

def clients(request):
     return render(request,"clients.html")
def letstalk(request):
     return render(request,"letstotalk.html")