from django.shortcuts import render

# Create your views here.
def contion(request):
    d={'a':20,'b':30,'c':40}
    return render(request,'contions.html',context=d)
def forloop(request):
    d={'name':'ASHU'}
    return render(request,'forloop.html',d)
