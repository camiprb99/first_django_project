from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    role = models.CharField(max_length=32, choices=[(x, x) for x in ['Student', 'Profesor']])

class Classroom(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=200)
    state = models.CharField(max_length=30, choices=[(x, x) for x in ['ocupata', 'disponibila']])
    capacity = models.IntegerField()

class Reservation(models.Model):
    classroom = models.OneToOneField(Classroom, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reason = models.CharField(max_length=200)
    startdate = models.DateField()
    enddate = models.DateField()
