from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from .models import Bear, Feeding, Toy
from .forms import FeedingForm

class FeedingCreateView(CreateView):
    model = Feeding
    form_class = FeedingForm

class BearCreate(CreateView):
    model = Bear
    fields = '__all__'

class BearUpdate(UpdateView):
    model = Bear
    fields = ['breed', 'description', 'age']

class BearDelete(DeleteView):
    model = Bear
    success_url = '/bears/'

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = '__all__'

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

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
    feeding_form = FeedingForm()
    return render(request, 'bears/details.html', {'bear': bear, 'feeding_form': feeding_form})

def add_feeding(request, bear_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.bear_id = bear_id
        new_feeding.save()
    return redirect('detail', bear_id=bear_id)