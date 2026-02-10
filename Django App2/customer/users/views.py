from django.shortcuts import render

# Create your views here.
from .form import userFormData
from .models import Userform

def addUser(request):
    if request.method=="POST":
        form=userFormData(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=userFormData()
    users=Userform.objects.all()

    return render(request,'adduser.html',{'form':form,'users':users})

