from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import (
    CreateAPIView, ListAPIView, UpdateAPIView
)
from rest_framework.views import APIView
from .serializer import (
    UserSerializer,
    MyTokenObtainPairSerializer,
)
from .models import User
from rest_framework import status
from rest_framework.response import Response
from django.utils.http import (
    urlsafe_base64_decode,
    urlsafe_base64_encode
)
from django.utils.encoding import (
    force_text,
    force_bytes
)

class CreateUserView(CreateAPIView):
    """Апи для создания пользователей"""
    serializer_class = UserSerializer

create_user = CreateUserView.as_view()

class Login(TokenObtainPairView):
    """Логин"""
    serializer_class = MyTokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        email = self.request.data.get('email').lower()
        user = User.objects.filter(email=email)
        if not user:
            return Response(
                {"detail": "Пайдаланушы табылмады"},
                status=status.HTTP_400_BAD_REQUEST)
        return super().post(request, *args, **kwargs)

login = Login.as_view()

class UserListView(ListAPIView):
    """Вывод всех пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()

list_user = UserListView.as_view()