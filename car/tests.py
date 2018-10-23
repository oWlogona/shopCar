from django.test import TestCase
from django.core.exceptions import ValidationError
from django.test import Client
# Create your tests here.


from car.models import validate_longtitude


class TestValidators(TestCase):

    def test_validate_longtitude(self):
        valid_long = [89.01, 0.00, -89.9]
        for val in valid_long:
            validate_longtitude(val)


    def test_not_valide_longtitude(self):
        not_valid_long = [91.00, 180.00, 152.06, -105.01, -90.01]
        for val in not_valid_long:
            with self.assertRaises(ValidationError):
                validate_longtitude(val)

    '''
    def test_endpoint(self):
        # Дописать тест.
        # 1) Создать данные моделей для теста.
        Car.objects.create(

        )

        client = Client()
        response = client.get('/cars/')
    '''

