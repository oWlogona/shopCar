from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from userprofile_auth.serializers import UserSerializer
from rest_framework.authtoken.models import Token


class UserSignIn(APIView):

    def post(self, request, *args, **kwargs):
        user = authenticate(request, username=request.data.get('username'), password=request.data.get('password'))
        if user:
            token, created = Token.objects.get_or_create(user=user)
            content = {
                'user': user.username,
                'token': token.key,
            }
            serializer = UserSerializer(data=content)
            if serializer.is_valid():
                return Response(serializer.data)
            return Response(serializer.errors)
        return HttpResponse('DoesNotUser')
