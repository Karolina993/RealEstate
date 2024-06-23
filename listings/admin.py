from django.contrib import admin
from .models import Listing

class ProfileAdmin(admin.ModelAdmin):
    User_list = ['username', 'email']


admin.site.register(Listing)