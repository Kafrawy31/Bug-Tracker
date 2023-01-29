from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('home')

def login(request):
    return HttpResponse('login')

def account(request):
    return HttpResponse('account')

def bugs(request):
    return HttpResponse('bugs')


