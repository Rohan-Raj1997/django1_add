from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'home.html')

def add(request):
    v1=int(request.GET['num1'])
    v2=int(request.GET['num2'])
    res=v1+v2
    return render(request,'result.html',{'result':res})
    # {{ csrf_token}}


