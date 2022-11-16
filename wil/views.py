from django.shortcuts import render
from django.http import HttpResponse
from .functions import handle_uploaded_file
from .forms import RegistrationForm

from . import models
# Create your views here.

def register_wil(request):

	if request.POST:
		user = request.user
		student_number = request.POST['student_number']
		department = request.POST['department']
		uploaded_file = request.FILES['uploaded_file']

		register = models.Registration(student_number=student_number,department=department, uploaded_file=uploaded_file, user=user)
		register.save() 
		handle_uploaded_file(request.FILES['uploaded_file'])
		return HttpResponse('Successfully registered')

	else:

		context = {'RegistrationForm' : RegistrationForm,
		}
		return render(request, 'wil/register_wil.html',context)

def instractions(request):
	return render(request, 'wil/instractions.html',{})
