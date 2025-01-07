from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ("id", "email", "username", "first_name", "last_name", "phone", "address","is_active")
        read_only_fields = ("id", "is_active")
    

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators= [validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("email", "username", "password", "password2", "first_name", "last_name", "phone","address")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop("password2")
        user = User(**validated_data)
        user.set_password("password")
        user.save()
        return user

class ChangePasswordSerializer(serializers.ModelSerializer):

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
    new_password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs["new_password"] != attrs["new_password"]:
            return serializers.ValidationError({"password": "password fields didn't match."})
        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = UserSerializer(self.user).data
        return data
    


