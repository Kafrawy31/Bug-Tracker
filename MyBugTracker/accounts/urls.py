from django.urls import path
from . import views
urlpatterns = [
    path('', views.login),
    path('home/', views.home),
    path('user/<str:pk>/', views.user),
    path('ticket/<str:ptk>/', views.tickets, name='ticket_detail'),
    path('projects/<str:ppk>/', views.projects)
]
