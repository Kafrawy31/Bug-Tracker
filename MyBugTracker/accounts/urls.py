from django.urls import path
from . import views
urlpatterns = [
    path('', views.login),
    path('home/', views.home),
    path('account', views.account),
    path('bugs/', views.bugs)
]
