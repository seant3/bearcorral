from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from .models import Bear

class BearCreate(CreateView):
    model = Bear
    fields = '__all__'

class BearUpdate(UpdateView):
    model = Bear
    fields = ['breed', 'description', 'age']

class BearDelete(DeleteView):
    model = Bear
    success_url = '/bears/'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bears_index(request):
    bears = Bear.objects.all()
    return render(request, 'bears/index.html', {'bears': bears})

def bears_detail(request, bear_id):
    bear = Bear.objects.get(id=bear_id)
    return render(request, 'bears/details.html', {'bear': bear})