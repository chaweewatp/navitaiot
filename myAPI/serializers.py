from rest_framework import serializers
from django.contrib.auth.models import User


class UserSigninSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
