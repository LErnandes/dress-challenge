from django.db import models


class Phone(models.Model):
    number = models.CharField(max_length=11)

    def __str__(self):
        return self.number

class Address(models.Model):
    address = models.CharField(max_length=40)

    def __str__(self):
        return self.address

class Customer(models.Model):
    email = models.EmailField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.ManyToManyField(Phone, blank=True)
    address = models.ManyToManyField(Address, blank=True)
