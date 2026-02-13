from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import StudentProfiles

from django.contrib.auth import authenticate, login, logout

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']
        if password == confirm_password:
            user = User.objects.create_user(username=username, password=password)
            StudentProfiles.objects.create(user=user)
            return redirect('user_login')
    return render(request, 'user_register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'user_login.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    return redirect('user_login')



