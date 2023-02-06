from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8,write_only=True)

    class Meta:
        model = User
        fields = '__all__'
    
    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"]).exists()
        
        if email_exists:
            raise ValidationError("Email has already been used")

        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
            )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user