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

def user(request, pk):
    cuser = DevUser.objects.get(UserId=pk)
    user_tickets = cuser.assignedto.all()
    context = {'cuser': cuser, 'user_tickets':user_tickets}
    return render(request, 'accounts/user.html',context)

def tickets(request,ptk):
    cticket = Ticket.objects.get(TicketId=ptk)
    context = {'cticket': cticket}
    return render(request, 'accounts/tickets.html',context)

def projects(request,ppk):
    cproject = Ticket.objects.get(TicketId=ppk)
    project_tickets = cproject.tproject.all()
    context = {'cproject': cproject, 'project_tickets': project_tickets}
    return render(request, 'accounts/projects.html',context)



