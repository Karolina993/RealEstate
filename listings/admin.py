from django.contrib import admin
from .models import Listing, Profile

class ProfileAdmin(admin.ModelAdmin):
    User_list = ['username', 'email']


admin.site.register(Listing)
admin.site.register(Profile, ProfileAdmin)