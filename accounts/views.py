from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register.html')
            else:
                user = User.objects.create_user(username=username, password=password,)
                user.save()
                messages.success(request, 'Registration successful')
                return redirect('accounts:login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        messages.error(request, 'Please fill all the fields')
        return render(request, 'register.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('bank:single')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('accounts:login')
    else:
        return render(request,'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')