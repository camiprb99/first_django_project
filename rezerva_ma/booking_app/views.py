from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

classrooms = [
    {
        'state' : 'disponibila',
        'capacity' : 300
    }
]

# Create your views here.
def home(request):
    context = {
        'classrooms' : classrooms
    }
    # return HttpResponse('<h1>Home</h1>')
    return render(request, 'home.html', context)

def register(request):
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})