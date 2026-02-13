from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import StudentProfiles

from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']
        if password == confirm_password:
            user = User.objects.create_user(username=username, password=password)
            StudentProfiles.objects.create(user=user)
            return redirect('login')
    return render(request, 'register.html')



