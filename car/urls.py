from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from car.views import CarDetail, CarList, UserList, UserDetail, CarFilterModel, api_root

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('cars/', CarList.as_view(), name="cars-list"),
    path('cars/<int:pk>/', CarDetail.as_view()),
    path('users/', UserList.as_view(), name="users-list"),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('cars/<str:model>/', CarFilterModel.as_view())
])
