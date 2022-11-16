from django.forms import ModelForm
from django import forms

from .models import Registration


class RegistrationForm(ModelForm):
	student_number = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'student number',

		}))

	uploaded_file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))

	# department = forms.ChoiceField(widget=forms.Select(attrs={
	# 	'class': 'form-control',
	# 	}))
	
	class Meta:
		model = Registration
		fields = ('user', 'student_number', 'department', 'uploaded_file')
	