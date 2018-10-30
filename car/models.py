from django.db import models
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError


def validate_longtitude(value):
    if value >= 90 or value <= -90:
        raise ValidationError('(value)s longitude must be to -90 from 90'.format(value=value))


def validate_latitude(value):
    if value >= 180 or value <= -180:
        raise ValidationError('(value)s latitude must be to -180 from 180'.format(value=value))


class ModelCar(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class BrandCar(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class TransmissionCar(models.Model):
    TYPE_TRANSMISSION = (
        ('AUTO', 'AUTOMATIC'),
        ('MAN', 'MANUAL'),
    )
    t_type = models.CharField(max_length=20, choices=TYPE_TRANSMISSION,
                              default={None: 'YOUR CARS TRANSMISSION'})  # choices ()

    def __str__(self):
        return self.t_type


class City(models.Model):
    name = models.CharField(max_length=20)
    longitude = models.FloatField(default=0, validators=[validate_longtitude])
    latitude = models.FloatField(default=0, validators=[validate_latitude])

    def __str__(self):
        return self.name


class Car(models.Model):
    owner = models.ForeignKey(User, related_name='cars', on_delete=models.CASCADE)
    created_by = models.DateTimeField(auto_now_add=True)
    model = models.ForeignKey(ModelCar, on_delete=models.CASCADE, blank=True, null=True, default=None)
    brand = models.ForeignKey(BrandCar, on_delete=models.CASCADE, blank=True, null=True, default=None)
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=20, blank=True, null=True, default=None)
    transmission = models.ForeignKey(TransmissionCar, on_delete=models.CASCADE, blank=True, null=True, default=None)
    city = models.ManyToManyField(City, related_name='city_car', blank=True, default=None)
