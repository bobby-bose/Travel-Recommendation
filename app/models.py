from django.db import models
from django.contrib.auth.models import User

class TravelPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    num_travelers = models.IntegerField()
    num_female_travelers = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Travel Preference to {self.destination}"

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    amenities = models.TextField()
    # Add other fields as needed

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price_range = models.CharField(max_length=20)
    # Add other fields as needed

    def __str__(self):
        return self.name
