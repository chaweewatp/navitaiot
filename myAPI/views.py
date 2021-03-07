from django.shortcuts import render
from django.http import HttpResponse


from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)


from rest_framework.authtoken.models import Token
from myAPI.authentication import token_expire_handler
from django.contrib.auth import authenticate
from myAPI.serializers import UserSigninSerializer
# Create your views here.


# def signin(request):
#     if request.method == "POST":
#         print('method = POST')
#         # check if username and password is valid
#
#         signin_serializer = UserSigninSerializer(data=request.POST)
#         print(request.POST)
#         if not signin_serializer.is_valid():
#             return HttpResponse('invalid input')
#             # return Response(signin_serializer.errors, status=HTTP_400_BAD_REQUEST)
#         user = authenticate(
#             username=request.POST.get("username"),
#             password=request.POST.get("password")
#         )
#         print(not user)
#         if not user:
#             return HttpResponse('Invalid Credentials or activate account')
#
#             # return Response({'detail': 'Invalid Credentials or activate account'}, status=HTTP_404_NOT_FOUND)
#         # TOKEN STUFF
#
#         token, _ = Token.objects.get_or_create(user=user)
#         is_expired, token = token_expire_handler(token)  # The implementation will be described further
#         try:
#             # then go ot home and send farmID with valid token
#             print('login success')
#             token="0000000220020230"
#             return HttpResponse("OK")
#         except ValueError as e:
#             # else: popup error
#             return HttpResponse("login fail")
#             # return Response({"detial": 'Error on authentication'}, status.HTTP_401_UNAUTHORIZED)
#     return render(request, 'myFarm/index.html')


@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated

def test(request):
    return Response("Test")


def login(request):


    if request.method == "POST":
        print('method = POST')
        # check if username and password is valid
        signin_serializer = UserSigninSerializer(data=request.POST)
        print(request.POST)
        if not signin_serializer.is_valid():
            return HttpResponse('invalid input')
            # return Response(signin_serializer.errors, status=HTTP_400_BAD_REQUEST)
        user = authenticate(
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )
        print(not user)
        if not user:
            return HttpResponse('Invalid Credentials or activate account')

            # return Response({'detail': 'Invalid Credentials or activate account'}, status=HTTP_404_NOT_FOUND)
        # TOKEN STUFF

        token, _ = Token.objects.get_or_create(user=user)
        is_expired, token = token_expire_handler(token)  # The implementation will be described further
        try:
            # then go ot home and send farmID with valid token
            print('login success')
            return HttpResponse("OK")
        except ValueError as e:
            # else: popup error
            return HttpResponse("login fail")
            # return Response({"detial": 'Error on authentication'}, status.HTTP_401_UNAUTHORIZED)
    return render(request, 'myFarm/index.html')

