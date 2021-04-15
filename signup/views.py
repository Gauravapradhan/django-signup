from django.shortcuts import render,HttpResponse
from signup.models import Index

# Create your views here.
def index(request):
    if request.method=="POST":
       name=request.POST.get('name')
       email=request.POST.get('email')
       password=request.POST.get('password')
       index=Index(name=name,email=email,password=password)
    return render(request,"index.html")
def FP(request):
    return render(request,"FP.html")
def SetP(request):
    return render(request,"SetP.html")
    #return HttpResponse("")