from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, logout
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.shortcuts import render

from ..models import User

from .serializers import (LoginSerializer, RegisterAdminSerializer, UserResetChangePasswordSerializer, SpecificUserSerializer,
                          RegisterUserSerializer)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }

class UserLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data['email']
            password = serializer.data['password']
            user = authenticate(email=email, password=password)
            if(user is not None):
                # print(user.id)
                token = get_tokens_for_user(user)
                return Response({'message': 'login success', 'token': token}, status=status.HTTP_200_OK)
            else:
                try:
                    user_active = User.objects.get(email=email)
                except User.DoesNotExist:
                    return Response({'message': 'user not found mail'}, status=status.HTTP_404_NOT_FOUND)

                if not user_active.is_active:
                    return Response({'message': 'user account not active'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'message': 'The password is incorrect!'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'something went wrong!', 'error': serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)


class AdminRegisterView(APIView):
    # permission_classes = [IsAuthenticated, IsAdminUser]
    def post(self, request):
        serializer = RegisterAdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # instance_user = serializer.save()
            # instance_user.created_at = timezone.now().date()
            # instance_user.save()
            return Response({'message': 'registration successfully'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'something went wrong!', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class UserRegisterView(APIView):
    # permission_classes = [IsAuthenticated, IsAdminUser]
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # instance_user = serializer.save()
            # instance_user.created_at = timezone.now().date()
            # instance_user.save()
            return Response({'message': 'registration successfully'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'something went wrong!', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserChangePasswordView(APIView):
    # permission_classes = [IsAuthenticated]
    def put(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({'message': 'user not found!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserResetChangePasswordSerializer(user, data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            print(serializer.validated_data['password'])
            user.save()
            return Response({'message': 'successful updated password'}, status=status.HTTP_202_ACCEPTED)

        return Response({'message': 'something went wrong!', 'error': serializer.errors}, status=status.HTTP_404_NOT_FOUND)

class GetSpecificUserView(APIView):
    # permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({'message': 'user not found!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SpecificUserSerializer(user, context={"request": request})
        return Response({'message': 'user exist', 'data': serializer.data}, status=status.HTTP_200_OK)

