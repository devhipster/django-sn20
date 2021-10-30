from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'meeting/index.html')
    
def testing(request):
    
    return HttpResponse(' <h1>welcome to second attemp to finish a django course</h1>')