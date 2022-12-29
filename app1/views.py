from django.shortcuts import render

# Create your views here.
def first(request):
    
    d={'name':'ROCK'}
    
    return render(request,'one.html',context=d)