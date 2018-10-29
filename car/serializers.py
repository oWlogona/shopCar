from car.models import Car, City
from rest_framework import serializers
from django.contrib.auth.models import User


class CitySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    cars_in_city = serializers.IntegerField(default=0)
    brands = serializers.ListField()


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
