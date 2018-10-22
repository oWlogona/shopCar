from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


def validate_coors(val):
    if True:
        pass
    else:
        raise ValidationError


class ModelCar(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class BrandCar(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class TransmissionCar(models.Model):
    t_type = models.CharField(max_length=20)  # choices ()

    def __str__(self):
        return self.t_type


class City(models.Model):
    name = models.CharField(max_length=20)
    longtitude = models.FloatField(default=0, validators=[validate_coors])
    latitude = models.FloatField(default=0)

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
