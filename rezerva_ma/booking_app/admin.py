from django.contrib import admin
from .models import Profile, Classroom, Reservation

# Register your models here.
admin.site.register(Profile)
admin.site.register(Classroom)
admin.site.register(Reservation)