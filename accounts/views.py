from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            User.objects.create_user(username=username, password=password)
            return redirect('login')
    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('/')
