from django.test import TestCase
from .models import *


class CustomerTestCase(TestCase):
    def setUp(self):
        customer = Customer.objects.create(email="example@example.com", first_name="admin", last_name="example")
        Phone.objects.create(number=['11111111111'])
        Address.objects.create(address=['avenida 2'])

        customer.phone.add(Phone.objects.get(number=['11111111111']))
        customer.address.add(Address.objects.get(address=['avenida 2']))

        customer.save()


    def test_customer_required_fields(self):
        """Customer may have the required fields"""
        customer = Customer.objects.get(email="example@example.com")

        self.assertEqual(customer.email, 'example@example.com')
        self.assertEqual(customer.first_name, 'admin')
        self.assertEqual(customer.last_name, 'example')
    
    def test_customer_optional_fields(self):
        """Customer may have the optional fields"""
        customer = Customer.objects.get(email="example@example.com")
        phone = Phone.objects.get(number=['11111111111'])
        address = Address.objects.get(address=['avenida 2'])

        self.assertEqual(customer.phone.first().number, phone.number)
        self.assertEqual(customer.address.first().address, address.address)
