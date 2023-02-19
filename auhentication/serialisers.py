
from .models import User
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate


class UserCreationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=80, allow_blank=False)
    password = serializers.CharField(min_length=8, write_only=True)
    username = serializers.CharField(max_length=40, allow_blank=True)

    class Meta:
        model = User
        fields = ['id','username', 'email', 'password']

    # def validate(self, attrs):
    #     email = User.objects.filter(email=attrs.get('email')).exists()

    #     if email:
    #         raise ValidationError(detail="User with email exists", code=status.HTTP_403_FORBIDDEN)
        
    #     # password = User.objects.filter(password=attrs.get('password')).exists()

    #     # if password:
    #     #     raise ValidationError(detail="User with password exists", code=status.HTTP_403_FORBIDDEN)

    #     username = User.objects.filter(username=attrs.get('username')).exists()

    #     if username:
    #         raise ValidationError(detail="User with username exists", code=status.HTTP_403_FORBIDDEN)

    

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            )
        user.set_password(validated_data['password'])
        user.save()
        return user



class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError(_("Invalid email or password"))
            if not user.is_active:
                raise serializers.ValidationError(_("User account is disabled"))
            data['user'] = user
        else:
            raise serializers.ValidationError(_("Both email and password are required"))
        return data