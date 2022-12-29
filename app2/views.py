from django.shortcuts import render

# Create your views here.
def first(request):
    
    d={'name':'ROCK','sal':50000}
    
    return render(request,'two.html',context=d)