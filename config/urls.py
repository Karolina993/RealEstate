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
from listings.views import hello, SignUpView, ListingsView, ListingsChangeView, ListingsDeleteView, user_list
from listings.views import signup


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_list/', views.user_list, name='user_list'),
    path('listings/', include('listings.urls')),
    path('accounts/sign_up', SignUpView.as_view(), name='sign_up'),
    path('accounts/login', include('listings.urls')),
    path('accounts/logout/', include('listings.urls')),
    path('change/<pk>', ListingsChangeView.as_view(), name='change'),
    path('delete/<pk>',ListingsDeleteView.as_view(), name='delete'),

]
