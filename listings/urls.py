from django.urls import path
from . import views

urlpatterns = [
    path('listings',views.listing_list,name="listing_listlist")
]