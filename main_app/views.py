from django.shortcuts import render
from django.http import HttpResponse

class Bear:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

bears = [
    Bear('BoBo', 'Grizzly', 'Good cuddler', 10),
    Bear('Big Earn', 'Kodiak', 'You may want to run', 13),
    Bear('Snowy', 'Polar', 'Awwwww', 1)
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bears_index(request):
    return render(request, 'bears/index.html', {'bears': bears})