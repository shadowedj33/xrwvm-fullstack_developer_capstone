# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # color = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CarModel(models.Model):

    CAR_CHOICES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
    ]
        
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=CAR_CHOICES, default='SUV')
    year = models.IntegerField(default=2023,
        validators = [
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])

    def __str__(self):
        return self.name
