from django.test import TestCase
from car.models import Car
from car.models import validate_latitude, validate_longtitude


class CarModelTestCase(TestCase):

    def setUp(self):
        Car.objects.create(owner_id=1, brand_id=1, price=1470, color='YELLOW', transmission_id=1)
        Car.objects.create(owner_id=2, brand_id=2, price=2470, color='BLACK', transmission_id=2)
        Car.objects.create(owner_id=3, brand_id=3, price=3470, color='GREEN', transmission_id=3)

    def test_get_count_fields(self):
        self.assertEqual(Car.objects.count(), 3)


class TestValidatorsTestCase(TestCase):

    def setUp(self):
        self.valid_long = [89.01, 0.00, -89.9]
        self.not_valid_long = [91.00, 180.00, 152.06, -105.01, -90.01]

    def test_validate_longtitude(self):
        for val in self.valid_long:
            validate_longtitude(val)

    def test_not_valide_longtitude(self):
        for val in self.not_valid_long:
            with self.assertRaises(Exception):
                validate_longtitude(val)


class EndPointTestCase(CarModelTestCase):

    def test_my_think(self):
        print('here', Car.objects.count())
