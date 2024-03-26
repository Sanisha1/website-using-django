from django.shortcuts import render,   HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        "variable":"this is sent"
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is services page")

def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        contact= Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your message have been sent!")
    return render(request,'contact.html')
    #return HttpResponse("this is contact page")