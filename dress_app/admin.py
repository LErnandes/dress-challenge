from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['email', 'first_name', 'last_name']


class PhoneAdmin(admin.ModelAdmin):
    search_fields = ['number']


class AddressAdmin(admin.ModelAdmin):
    search_fields = ['address']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Address, AddressAdmin)
