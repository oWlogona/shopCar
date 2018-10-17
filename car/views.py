from django.http import Http404
from car.serializers import CarSerializer
from car.models import Car
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class CarDetail(APIView):

    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Http404

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
