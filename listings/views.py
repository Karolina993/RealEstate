from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
import listings
from .models import Listing
from .forms import AdsForm
from .forms import ListingSearchForm

def hello(request):
    return HttpResponse('<h1>Welcome to the Home Page</h1>')

#@login_required
class ListingsView(LoginRequiredMixin, ListView):
    template_name = 'listings.html'
    context_object_name = 'listings'
    model = Listing
    # fields = ['title', 'location', 'price',  'photo_main', 'user']
    permission_required = 'listings_viewer.view_listings'
    #
    # def get_queryset(self):
    #     return Listing.objects.filter(user=self.request.user)
    #
    # def get(self, request, *args, **kwargs):
    #     listing_id = kwargs.get('pk')
    #     if listing_id:
    #         listing = get_object_or_404(Listing, id=listing_id, user=request.user)
    #         listing.no_clicks += 1
    #         listing.save()
    #     return super().get(request, *args, **kwargs)

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

# class ListingsView(LoginRequiredMixin, ListView):
#     template_name = 'list.html'
#     model = listings
#     login_url = 'login'
#     success_url = reverse_lazy('index')
#     permission_required = 'listing_viewer.view_listing'

    # def get(self, request, *args, **kwargs):
    #     profile = Profile.objects.get(user=request.user)
    #     profile.no_clicks += 1
    #     profile.save()
    #     return super().get(request, args, kwargs)

#@login_required
class ListingsAddView(LoginRequiredMixin,CreateView):
        form_class = AdsForm
        template_name = 'form.html'
        model = listings
        login_url = 'login'
        success_url = reverse_lazy('index')
#       permission_required = 'listing_viewer.add_listing'

# def ListingsAddView(request):
#     if request.method == 'POST':
#         form = ListingsAddView(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('login')
#     else:
#       form = ListingsAddView()
#     return render(request, 'registration/login.html', {'form': form})

class ListingsChangeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Listing
    template_name = 'listing_edit.html'
    fields = ['title','location', 'description','price', 'rooms', 'sqft', 'photo_main', 'is_published', 'is_booked', 'posted', 'user']
    form_class = AdsForm
    success_url = reverse_lazy('index')
    permission_required = 'listing_viewer.change_listing'

    def test_func(self):
        listing = self.get_object()
        return self.request.user == listing.user



class IsSuperuserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class ListingsDeleteView(IsSuperuserMixin, DeleteView):
    model = listings
    template_name = 'delete.html'
    success_url = reverse_lazy('index')





class ListingSearchView(ListView):
    model = Listing
    template_name = 'listing_search.html'
    context_object_name = 'listings'

    def get_queryset(self):
        queryset = Listing.objects.all()
        form = ListingSearchForm(self.request.GET)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            min_price = form.cleaned_data.get('min_price')
            max_price = form.cleaned_data.get('max_price')
            location = form.cleaned_data.get('location')
            rooms = form.cleaned_data.get('rooms')

            if title:
                queryset = queryset.filter(title__icontains=title)
            if min_price:
                queryset = queryset.filter(price__gte=min_price)
            if max_price:
                queryset = queryset.filter(price__lte=max_price)
            if location:
                queryset = queryset.filter(location__icontains=location)
            if rooms:
                queryset = queryset.filter(rooms=rooms)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ListingSearchForm(self.request.GET)
        return context

class ListingDetailsView(DetailView):
    model = Listing
    template_name = 'listing_details.html'
    context_object_name = 'listing'

 