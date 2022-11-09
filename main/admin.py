from django.contrib import admin
from .models import Student, Coordinator, Register, Department

admin.site.register(Student)
admin.site.register(Coordinator)
admin.site.register(Register)
admin.site.register(Department)

# Register your models here.
