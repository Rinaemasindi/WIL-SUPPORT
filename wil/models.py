from django.db import models
from django.contrib.auth.models import User

class Registration(models.Model):
	
	DEPT_CHOICES = (
        ('Computer Science', 'Computer Science'),
        ('Computer Systems Engineering', 'Computer Systems Engineering'),
        ('Informatics', 'Informatics'),
        ('Information Technology', 'Information Technology'),
    )

	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
	student_number = models.CharField(max_length=200)
	department = models.CharField(max_length=100, default="", choices=DEPT_CHOICES)	
	uploaded_file = models.FileField(default="")
	
	def __str__(self):
 		return self.student_number

