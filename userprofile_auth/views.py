from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from userprofile_auth.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import authenticate


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
                return Response({
                    'about_user': reverse('about_user', request=self.request, format=None),
                    'token': token.key,
                })
            return Response(serializer.errors)
        return HttpResponse('DoesNotUser')


class UserLogOut(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        Token.objects.get(user=request.user).delete()
        return Response(status=204)


class UserSomeDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token = get_object_or_404(Token, user=request.user)
        if token:
            content = {
                'user': request.user.username,
                'token': token.key,
            }
            serializer = UserSerializer(data=content)
            if serializer.is_valid():
                return Response(serializer.data)
            return Response(serializer.errors)
        return HttpResponse('Does Not Token of User')
