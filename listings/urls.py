from django.urls import path
from . import views

urlpatterns = [
    #path('', views.ListingsView(), name='listings'),
    path('user_list/', views.user_list, name='user_list'),
]
