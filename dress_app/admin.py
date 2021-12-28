from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    def full_name(self, customer):
        return f'{customer.first_name} {customer.last_name}'
    list_display = ('email', 'full_name')
    search_fields = ['email', 'first_name', 'last_name', 'phone__number', 'address__address']


class PhoneAdmin(admin.ModelAdmin):
    search_fields = ['number']


class AddressAdmin(admin.ModelAdmin):
    search_fields = ['address']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Address, AddressAdmin)
