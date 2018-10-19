from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from car.views import CarDetail, CarList, UserList, UserDetail, api_root

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('cars_list/', CarList.as_view(), name="cars-list"),
    path('cars_list/<int:pk>/', CarDetail.as_view()),
    path('users_list/', UserList.as_view(), name="users-list"),
    path('users_list/<int:pk>/', UserDetail.as_view()),
])
