from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from car.views import CarDetail

urlpatterns = format_suffix_patterns([
    path('car/<int:pk>', CarDetail.as_view()),
])