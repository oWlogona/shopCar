from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from car.views import CarDetail, CarList, UserList, UserDetail

urlpatterns = format_suffix_patterns([
    path('cars/', CarList.as_view()),
    path('cars/<int:pk>/', CarDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
])
