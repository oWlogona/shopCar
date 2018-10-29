from django.urls import path
from userprofile_auth.views import UserSignIn
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('', UserSignIn.as_view()),
])
