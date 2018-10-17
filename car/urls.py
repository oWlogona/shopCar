from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from car import views
from car.views import *

urlpatterns = format_suffix_patterns([
    path('carslist/', views.CarList.as_view()),
])