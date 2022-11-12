from django.forms import ModelForm
from django import forms
from .models import Student, Register

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'student_number', 'email', 'password')


class RegisterForm(ModelForm):
    

    # department_name = forms.FileField(widget=forms.FileInput(attrs={'class': ''}))
    # document = forms.MultipleChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=DEPT_CHOICES)
    class Meta:
        model = Register
        fields = ('department_name', 'document')
        
        # widgets = {
        #     'department_name': forms.FileInput(attrs={'class': 'form-class'}),
        #     'document': forms.SelectInput(attrs={'class': 'form-class'})
        # }