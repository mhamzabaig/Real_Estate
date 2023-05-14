from django.db import models

# Create your models here.

class Listing(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    no_of_bedrooms = models.IntegerField()
    no_of_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)
    # image = models.ImageField()

def __str__(self):
    return self.title