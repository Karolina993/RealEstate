from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from .models import Listing

class UserIsOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        listing_title = self.kwargs.get('title')  # Pobierz identyfikator ogłoszenia z URL
        listing = get_object_or_404(Listing, pk=listing_tite)
        return self.request.user == listing.user