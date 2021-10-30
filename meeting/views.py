from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    meets = [ 
        {'title':'first meeting','description':'A simple and first description'},
        {'title':'second meeting','description':'A second description'},
        {'title':'third meeting','description': 'A third description'}
    ]
    return render(request,'meeting/index.html',{'meeting':meets})
    
def testing(request):
    
    return HttpResponse(' <h1>welcome to second attemp to finish a django course</h1>')