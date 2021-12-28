from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import *


def index(request):
    name = request.GET.get('name', None)

    def getFields(model, exceptions=[]):
        return [field.name for field in model._meta.get_fields() if field.name not in exceptions]

    customers = Customer.objects.filter(Q(first_name=name) | Q(last_name=name)) if name is not None else Customer.objects.all()
    
    address = [{"customer": f'{customer.first_name} {customer.last_name}', "address": [add.address for add in customer.address.all()]} for customer in customers.all()]

    context = {
        "author": "Luis Ernandes",
        "customer_header": getFields(Customer, ['phone', 'address']),
        "customers": customers,
        "address_header": getFields(Address, ['id']),
        "address": address,
    }
    
    return render(request, "index.html", context)

def health(request):
    return HttpResponse()
