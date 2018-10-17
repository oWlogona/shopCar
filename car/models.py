from django.db import models


class ModelCar(models.Model):
    name = models.CharField(max_length=20)


class BrandCar(models.Model):
    name = models.CharField(max_length=20)


class TransmissionCar(models.Model):
    t_type = models.CharField(max_length=20)


class CityCar(models.Model):
    name = models.CharField(max_length=20)


class Car(models.Model):
    model = models.ForeignKey(ModelCar, on_delete=models.CASCADE,  blank=True, null=True, default=None)
    brand = models.ForeignKey(BrandCar, on_delete=models.CASCADE, blank=True, null=True, default=None)
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=20)
    transmission = models.ForeignKey(TransmissionCar, on_delete=models.CASCADE, blank=True, null=True, default=None)
    city = models.ManyToManyField(CityCar)




