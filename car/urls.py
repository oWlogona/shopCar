from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from car.views import CarDetail, CarList

urlpatterns = format_suffix_patterns([
    path('cars/', CarList.as_view()),
    path('cars/<int:pk>/', CarDetail.as_view()),
])
