from django.shortcuts import render
from .models import Listing
# Create your views here.
# CRUD + List will be our actions

def listing_list(request): # naming convention of view as "model_name"_"action_name"
    listings = Listing.objects.all()
    context = {
        'listings':listings
    }
    return render(request,'listings.html',context)
