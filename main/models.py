from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    student_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    IsRegistered = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + self.last_name
    


class Coordinator(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    office_address = models.CharField(max_length=200)
    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    

    def __str__(self):
        return self.first_name +" "+ self.last_name
    

class Register(models.Model):
    document = models.FileField()
    # department = 
    student_id = models.ForeignKey("Student", on_delete=models.SET_NULL) 

    def __str__(self):
        return self.pk
    


class Department(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name
    