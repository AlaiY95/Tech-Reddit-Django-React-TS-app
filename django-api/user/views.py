from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import User
from .serializers import (
    RegisterSerializer,
    CustomTokenObtainPairSerializer,
)


class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(CreateAPIView):
    # Django created an user instance from this
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )

    def create(self, request, *args, **kwargs):
        serializer: RegisterSerializer = self.get_serializer(data=request.data)
        # is.valid checks if the data is valid. Always do!
        serializer.is_valid(raise_exception=True)

        # Calling user instance from serializer.py
        user: User = serializer.create(
            validated_data=serializer.validated_data
        )
        refresh = CustomTokenObtainPairSerializer.get_token(user)
        
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
 

