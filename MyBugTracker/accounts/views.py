from django.shortcuts import render
from django.http import HttpResponse
import json
import sqlite3
from .models import *

def home(request):
    tickets = Ticket.objects.all()
    projects = Project.objects.all()
    OpenTickets = tickets.filter(TicketStatus = 'OP').count()
    PendingTickets = tickets.filter(TicketStatus = 'PE').count()
    VhighPrio = tickets.filter(TicketPriority = "VH").count()
    HighPrio = tickets.filter(TicketPriority = "H").count()
    MediumPrio = tickets.filter(TicketPriority = "M").count()
    LowPrio = tickets.filter(TicketPriority = "L").count()
    stats = {'tickets':tickets,
             'projects':projects,
             'OpenTickets':OpenTickets,
             'PendingTickets':PendingTickets,
             'VhighPrio':VhighPrio,
             'HighPrio':HighPrio,
             'MediumPrio':MediumPrio,
             'LowPrio':LowPrio}
    return render(request, 'accounts/home.html', stats)

def login(request):
    return render(request, 'accounts/login.html')

def user(request):
    return render(request, 'accounts/user.html')

def tickets(request):
    return render(request, 'accounts/user.html')




