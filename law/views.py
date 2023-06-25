from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse
from datetime import datetime
from law.models import info

# Create your views here.
def index(request):
    return render(request,'index.html')
def rights(request):
    return render(request,'rights.html')
    

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        Date= info(name=name,email=email,phone=phone,desc=desc, date=datetime.today())
        Date.save()

        

    return render(request,'contact.html')
    
def about(request):
    return render(request,'about.html')
    
