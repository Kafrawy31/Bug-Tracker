from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'accounts/home.html')

def login(request):
    return render(request, 'accounts/login.html')

def user(request):
    return render(request, 'accounts/user.html')




