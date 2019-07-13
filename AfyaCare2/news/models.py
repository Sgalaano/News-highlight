from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    avatar = models.ImageField(upload_to='photos/',null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length = 50)
    medicalId = models.CharField(max_length =10)
    bio = models.TextField(null=True)
    email = models.EmailField(max_length = 60, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.name

class Doctors(models.Model):
    LOCATIONS = (
    ('Westlands','Westlands',),
    ('Dagoretti','Dagoretti'),
    ('Kibra', 'Kibra'),
    ('Roysambu', 'Roysambu'),
    ('Kasarani', 'Kasarani'),
    ('Ruaraka', 'Ruaraka'),
    ('Embakasi', 'Embakasi'),
    ('Madaraka', 'Madaraka'),
    ('Kamukunji', 'Kamukunji'),
    ('Starehe', 'Starehe'),
    ('Mathare', 'Mathare'),
    )
    DOCTORTYPE = (
    ('Family Doctor' , 'Family Doctor',),
    ('Dermatologist' , 'Dermatologist',),
    ('Psychiatrist','Psychiatrist'),
    ('Gynecologist' ,'Gynecologist'),
    ('Other' , 'Other'),
    )
    name = models.CharField(max_length = 50)
    Location = models.CharField(max_length = 50,choices=LOCATIONS) 
    doctype = models.CharField(max_length = 60, choices= DOCTORTYPE)
    email = models.CharField(max_length = 60)
    photo_image = models.ImageField(upload_to = 'photos/')

    def __str__(self):
        return self.name
    def save_doctors(self):
        self.save()
    @classmethod
    def get_doctors(cls):
        doctors = Doctors.objects.all()
        return doctors

    

class Patients(models.Model):
    LOCATIONS = (
    ('Westlands','Westlands',),
    ('Dagoretti','Dagoretti'),
    ('Kibra', 'Kibra'),
    ('Roysambu', 'Roysambu'),
    ('Kasarani', 'Kasarani'),
    ('Ruaraka', 'Ruaraka'),
    ('Embakasi', 'Embakasi'),
    ('Madaraka', 'Madaraka'),
    ('Kamukunji', 'Kamukunji'),
    ('Starehe', 'Starehe'),
    ('Mathare', 'Mathare'),
    )
    name = models.CharField(max_length = 50)
    Location = models.CharField(max_length = 50,choices=LOCATIONS)
    email = models.CharField(max_length = 60)
    photo_image = models.ImageField(upload_to = 'photos/')