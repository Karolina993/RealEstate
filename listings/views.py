from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
import listings
from .models import Listing, Profile
from .forms import AdsForm

def hello(request):
    return HttpResponse('<h1>Welcome to the Home Page</h1>')

class ListingList(PermissionRequiredMixin, ListView):
    template_name = 'listings.html'
    model = listings
    #permission_required = 'stock_viewer.view_stock'
@login_required

def listing_list(request):
    Listing.objects.all()
    if request.method == 'POST':
        form = AdsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('list')
    else:
         form = AdsForm()
    return render(request, 'registration/login.html', {'form': form})
   # return render(request, 'listings.html', {'listings': listings})

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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('add')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('hello')
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

from django.contrib.auth.mixins import LoginRequiredMixin

#@login_required
class ListingsAddView(LoginRequiredMixin,CreateView):
        form_class = AdsForm
        template_name = 'form.html'
        model = listings
        login_url = 'login'
        success_url = reverse_lazy('index')
#        permission_required = 'listing_viewer.add_listing'

# def ListingsAddView(request):
#     if request.method == 'POST':
#         form = ListingsAddView(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('login')
#     else:
#       form = ListingsAddView()
#     return render(request, 'registration/login.html', {'form': form})

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




