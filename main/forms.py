from django.forms import ModelForm
from .models import Student, Register

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'student_number', 'email', 'password')


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ('first_name', 'last_name', 'student_number', 'email', 'password')
        