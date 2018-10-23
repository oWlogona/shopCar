from django.test import TestCase
from car.models import Car
from django.test import Client


class CarTestCase(TestCase):

    def setUp(self):
        Car.objects.create(owner_id=1, brand_id=1, price=1470, color='YELLOW', transmission_id=2)
        Car.objects.create(owner_id=1, brand_id=2, price=2470, color='BLACK', transmission_id=1)

    def test_main_endpoint(self):
        client = Client()
        response = client.get('/cars/')
        print(response.content)

# from django.test import TestCase
# from car.models import Car
# from django.core.exceptions import ValidationError
# from django.test.client import Client
#
# # Create your tests here.
# from car.models import validate_longtitude
#
#
# class TestValidators(TestCase):
#     '''
#     def test_validate_longtitude(self):
#         valid_long = [89.01, 0.00, -89.9]
#         for val in valid_long:
#             validate_longtitude(val)
#
#     def test_not_valide_longtitude(self):
#         not_valid_long = [91.00, 180.00, 152.06, -105.01, -90.01]
#         for val in not_valid_long:
#             with self.assertRaises(Exception):
#                 validate_longtitude(val)
#     '''
#
#
# class TestValidators(Client):
#
#     def get(self, path, data=None, follow=False, secure=False, **extra):
#
#
# # def test_main_endpoint(self):
# #    Car.objects.create(owner_id=1, brand_id=1, price=1470, color='YELLOW', transmission_id=2)
# #    client = Client()
# #    response = client.get('/cars/')
