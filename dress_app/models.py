from django.db import models


class Phone(models.Model):
    number = models.CharField(max_length=11)

class Address(models.Model):
    address = models.CharField(max_length=40)

class Customer(models.Model):
    email = models.EmailField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.ManyToManyField(Phone)
    address = models.ManyToManyField(Address)
