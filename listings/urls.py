from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_list, name='listings-home'),
    path('user_list/', views.user_list, name='user_list'),
]
