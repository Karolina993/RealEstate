from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin

from django.shortcuts import render, redirect
from .forms import SignUpForm

import listings
from .models import Listing, Profile
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

class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('hello')

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

class ListingsView(PermissionRequiredMixin, ListView):
    template_name = 'list.html'
    model = listings
    permission_required = 'listing_viewer.view_listing'

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        profile.no_clicks += 1
        profile.save()
        return super().get(request, args, kwargs)


class ListingsAddView(PermissionRequiredMixin, CreateView):
    form_class = AdsForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')
    permission_required = 'listing_viewer.add_listing'


class ListingsChangeView(PermissionRequiredMixin, UpdateView):
    model = listings
    template_name = 'form.html'
    form_class = AdsForm
    success_url = reverse_lazy('index')
    permission_required = 'listing_viewer.change_listing'

class IsSuperuserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class ListingsDeleteView(IsSuperuserMixin, DeleteView):
    model = listings
    template_name = 'delete.html'
    success_url = reverse_lazy('index')


