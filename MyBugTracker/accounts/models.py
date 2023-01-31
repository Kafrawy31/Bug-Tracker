from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Ticket(models.Model):
    class TPriority(models.TextChoices):
        VHigh = 'VH', "Very Important"
        High = 'H', "Important"
        Medium = 'M', "Medium"
        Low = 'L', "Low"
    class TStatus(models.TextChoices):
        Open = 'OP', "Open"
        Pending = 'PE', "Pending"
        Closed = 'CL', "Closed"
        
    TicketId = models.AutoField(primary_key=True)
    TicketDescription = models.CharField(max_length=255)
    TicketStatus = models.CharField(max_length=20, choices=TStatus.choices )
    TicketPriority = models.CharField(max_length=16,choices=TPriority.choices)
    TicketAssignedTo = models.CharField(max_length=30, null=True)
    TicketPoints = models.IntegerField(default=1,
                                       validators=[MaxValueValidator(10),
                                                   MinValueValidator(1)
        
    ])
    
class DevUser(models.Model):
    class UserRole(models.TextChoices):
        Developer = 'DEV', "Developer"
        Senior = 'SEN', "Senior"
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=26)
    UserEmail = models.EmailField(max_length=60)
    UserPassword = models.CharField(max_length=16)
    UserPoints = models.IntegerField(default=0)
    UserRole = models.TextField(max_length=12, choices=UserRole.choices, null=True)
class Project(models.Model):
    class PStatus(models.TextChoices):
        Finished = 'FI', "Finished"
        InProgress = 'IP', "InProgress"
        ComingUp = 'CU', "Coming Up"
    ProjectId = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=30)
    ProjectDescription = models.CharField(max_length=200)
    ProjectStatus = models.CharField(max_length=20, choices=PStatus.choices)
    
    
    