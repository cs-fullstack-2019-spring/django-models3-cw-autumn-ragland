from django.db import models
from datetime import date


# Book model with attributes and defaults
class Book(models.Model):
    name = models.CharField(max_length=200, default='')
    pageNumber = models.IntegerField(default=0)
    publishDate = models.DateField(default=date.today)
    genre = models.CharField(max_length=200, default='')

    # objects wil now display as their name
    def __str__(self):
        return self.name


# Car model with attributes and defaults
class Car(models.Model):
    make = models.CharField(max_length=200, default="")
    model = models.CharField(max_length=200, default="")
    year = models.DateField(default=date.today)

    # objects wil now display as their make
    def __str__(self):
        return self.make
