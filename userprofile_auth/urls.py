from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from userprofile_auth.views import UserSignIn, UserLogOut, UserSomeDetail

urlpatterns = format_suffix_patterns([
    path('', UserSignIn.as_view()),
    path('about_user/', UserSomeDetail.as_view(), name='about_user'),
    path('logout/', UserLogOut.as_view(), name='logout'),
])
