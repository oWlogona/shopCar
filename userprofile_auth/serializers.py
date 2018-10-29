from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=50)
    token = serializers.CharField(max_length=50)
