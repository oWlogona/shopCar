from django.contrib.auth.models import User
from car.models import Car
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Car
        fields = ('id', 'brand', 'price', 'color', 'transmission', 'city', 'model', 'owner')


class UserSerializer(serializers.ModelSerializer):
    cars = serializers.PrimaryKeyRelatedField(many=True, queryset=Car.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'cars')
