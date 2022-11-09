from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    coordinators = models.Coordinator.objects.all().order_by('last_name')

    context = { 'coordinators' : coordinators }

    return render(request, 'index.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)

def signup(request):
    context = {}
    return render(request, 'signup.html', context)


def register(request):
    context = {}
    return render(request, 'register.html', context)


def instractions(request):
    context = {}
    return render(request, 'instractions.html', context)
