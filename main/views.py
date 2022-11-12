from django.shortcuts import render
from . import models
from .forms import RegisterForm
from django.http import HttpResponse  
from .functions import handle_uploaded_file

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
    if  request.method == 'POST':

        # register = RegisterForm(request.POST, request.FILES)

        # if  register.is_valid():  
        #     handle_uploaded_file(request.FILES['document'])  
        #      

        x = request.FILES['document']
        y = request.POST['department_name']
        register = models.Register(department_name=x, document=y, student_id=1)
        register.save() 
        handle_uploaded_file(request.FILES['document'])
        return  HttpResponse("File uploaded successfuly")
    #     department = request.POST['department']
    #     file_name  = request.FILES['file_name']
    #     register = models.Register (department=department, document=file_name,is_registered=True)
    #     register.save()
    else:
        context = {'register_form' : RegisterForm}
        return render(request, 'register.html', context)


def instractions(request):
    context = {}
    return render(request, 'instractions.html', context)
