from django.shortcuts import render
#rest_framework related imports
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
#JWT imports
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .serializer import UserCreateSerializer, UserSerializer, ChangePasswordSerializer,CustomTokenObtainPairSerializer

User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action =="create":
            return [AllowAny()]
        return super().get_permissions()
    
    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer
        return UserSerializer

    @action(detail=False, methods=["get"])
    def me(self, request):
        self.get_serializer(request.user)
        return Response(serializer.data)

    @action(detail=False, methods=["put"])
    def update_profile(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial= True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @action(detail=True, methods=["post"])
    def change_password(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not user.check_password(serializer.validated_data["old_password"]):
            return Response(
                {"old_password": "wrong password"},
                status=status.HTTP_400_BAD_REQUEST
                    )
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        Response({"message": "password changed successfuly."})
