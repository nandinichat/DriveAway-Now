from django.db import models
# models.py

class Form(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

# Create your models here.
class Registration(models.Model):
    first_name = models.CharField(max_length=20)
    last_name =models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)

class Booking(models.Model):
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    pickup_date = models.DateField()
    dropoff_date = models.DateField()

