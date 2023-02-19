from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serialisers import UserCreationSerializer, UserSerializer
from drf_yasg.utils import swagger_auto_schema


class UserCreationView(generics.GenericAPIView):
    serializer_class = UserCreationSerializer

    @swagger_auto_schema(operation_summary='Create a user account')
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)




from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.http import JsonResponse


class SignInView(APIView):
    serializer_class = UserSerializer
    @swagger_auto_schema(operation_summary='Login a user account')
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})