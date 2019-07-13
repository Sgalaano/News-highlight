from django.contrib import admin
from .models import Profile, Doctors, Patients
# Register your models here.
admin.site.register(Profile)
admin.site.register(Doctors)
admin.site.register(Patients)