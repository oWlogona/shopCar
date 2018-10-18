from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from car.views import CarDetail, CarList

urlpatterns = format_suffix_patterns([
    path('car/<int:pk>/', CarDetail.as_view()),
    path('cars_list/', CarList.as_view()),
])