from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse(' welcome to second attemp to finish a django course')
    
def testing(request):
    
    return HttpResponse(' <h1>welcome to second attemp to finish a django course</h1>')