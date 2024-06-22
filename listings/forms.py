import django.forms

from django.db.models import Model, CharField, IntegerField, DecimalField, TextField, FileField, BooleanField, DateTimeField

from django.core.exceptions import ValidationError
from django.db.transaction import atomic

from . import models
from .models import Listing, image_path

# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    email = forms.EmailField()
@atomic
def save(self, commit=True):
        self.instance.is_active = True
        user = super().save(commit)
        profile = Profile(user=user, email=email)
        if commit:
            profile.save()
        return user
class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']



def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized')

class AdsForm(django.forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'

    # title = models.CharField(max_length=200)
    # location = models.TextField(max_length=128)
    # description = models.TextField(max_length=500)
    # price = models.IntegerField()
    # rooms = models.IntegerField()
    # sqft = models.IntegerField()
    # photo_main = models.FileField(upload_to=image_path)
    # is_published = models.BooleanField(default=True)
    # is_booked = models.BooleanField(default=False)
    # posted = models.DateTimeField(auto_now_add=True)
