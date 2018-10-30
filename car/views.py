from django.http import Http404
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework.response import Response
from car.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from car.models import Car, ModelCar, City, BrandCar
from car.serializers import CarSerializer, UserSerializer, CitySerializer

from django.db.models import Count


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users-list', request=request, format=format),
        'cars': reverse('cars-list', request=request, format=format),
        'city': reverse('city-list', request=request, format=format),
    })


class CarDetail(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request, format=None):
        cars_list = Car.objects.all()
        serializer = CarSerializer(cars_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(APIView):

    def get(self, request, format=None):
        users_list = User.objects.all()
        serializer = UserSerializer(users_list, many=True)
        return Response(serializer.data)


class UserDetail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class CarFilterModel(APIView):

    def get_object(self, model):
        try:
            return ModelCar.objects.get(name=model)
        except ModelCar.DoesNotExist:
            raise Http404

    def get(self, request, model, format=None):
        model_id = self.get_object(model)
        cars_filters_fields = Car.objects.filter(model=model_id.id)
        serializer = CarSerializer(cars_filters_fields, many=True)
        return Response(serializer.data)


class CityList(APIView):

    def get_brands_list(self, list_cars_in_city, all_brands_list):
        brand_car = {}
        for car_item in list_cars_in_city.select_related('brand'):
            brand_car[car_item.brand.name] = brand_car.get(car_item.brand.name, 0) + 1
        return brand_car

    def get(self, request, format=None):
        all_brands_list = BrandCar.objects.all()
        list_car = City.objects.annotate(count_car=Count('city_car'))
        cities_data = []
        for item in list_car:
            city_data = {
                'name': item.name,
                'cars_in_city': item.count_car,
                'brands': [],
            }
            city_data['brands'].append(self.get_brands_list(item.city_car.all(), all_brands_list))
            cities_data.append(city_data)
        serializer = CitySerializer(cities_data, many=True)
        return Response(serializer.data)
