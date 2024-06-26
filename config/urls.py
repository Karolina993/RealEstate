"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import listings
from listings import views
from listings import forms
from django.urls import include, path
from listings.views import SignUpView, ListingsView, ListingsChangeView, ListingsDeleteView, user_list, \
    ListingsAddView, ListingSearchView, ListingDetailsView, MyListingsView

from django.conf import settings
from django.conf.urls.static import static
from listings.views import signup, hello_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_list/', views.user_list, name='user_list'),
    path('listings/', include('listings.urls')),
    path('my_listings/', MyListingsView.as_view(), name='my_listings'),
    path('accounts/sign_up/', SignUpView.as_view(), name='sign_up'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('change/<str:pk>/', ListingsChangeView.as_view(), name='change'),
    path('list/<str:pk>/edit/', ListingsChangeView.as_view(), name='listing_edit'),
    path('list/<str:pk>/delete/', ListingsDeleteView.as_view(), name='delete'),
    path('hello/', views.hello_view, name='hello'),
    path('add/', ListingsAddView.as_view(), name='add'),
    path('list/', ListingsView.as_view(), name='index'),
    path('search/',ListingSearchView.as_view(), name='search'),
    path('details/<str:pk>/', ListingDetailsView.as_view(),name ='listing_details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

