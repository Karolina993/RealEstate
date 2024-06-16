from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .forms import SignUpForm

import listings
from .models import Listing
from .forms import AdsForm

def hello(request):
    return HttpResponse('<h1>Hello!</h1>')

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings.html', {'listings': listings})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/login.html', {'form': form})


class ConfigCreateView(CreateView):
    template_name = 'form.html'
    form_class = AdsForm
    success_url = reverse_lazy('form')


class ConfigUpdateView(UpdateView):
    template_name = 'form.html'
    form_class = AdsForm
    model = listings
    success_url = reverse_lazy('index')


class ConfigDeleteView(DeleteView):
    template_name = 'delete.html'
    model = listings
    success_url = reverse_lazy('index')
