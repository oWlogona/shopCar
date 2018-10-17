from django.shortcuts import render
from .models import CityCar, Car, TransmissionCar, ModelCar, BrandCar
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CarSerializer
# Create your views here.


class CarList(APIView):

    def get(self, request):
        carslist = Car.objects.all()
        serializer = CarSerializer(carslist, many=True)
        return Response(serializer.data)

