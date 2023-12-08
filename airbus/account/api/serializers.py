from rest_framework import serializers
import re

from ..models import User

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ['email', 'password']

class RegisterAdminSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'picture', 'gender']
        # exclude = ['created_at', 'otp', 'is_active', 'is_admin']
        extra_kwargs = {
            'picture': {'required': False},
            "gender": {'required': False}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_superuser(email=validated_data['email'],
                                             name=validated_data['name'],
                                             password=validated_data['password'])
        return user

    # def save(self):
    #     email = self.validated_data['email']
    #     password = self.validated_data['password']
    #     password2 = self.validated_data['password2']
    #     name = self.validated_data['name']
    #     gender = self.validated_data['gender']
    #     picture = self.validated_data.get('picture', 'user.png')
    #     is_active = self.validated_data['is_active']
    #     is_admin = self.validated_data['is_admin']
    #
    #     if not bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)):
    #         raise serializers.ValidationError({'message': 'Invalid email format!'})
    #
    #     if password != password2 :
    #         raise serializers.ValidationError({'message': 'password mismatch!'})
    #
    #     if not bool(re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$", password)):
    #         raise serializers.ValidationError({'message': 'password must contain least one digit, one uppercase letter, '
    #                                                       'at least one lowercase letter, at least one special character'})
    #
    #     if len(name) == 0:
    #         raise serializers.ValidationError({'message': 'name should not be empty!'})
    #
    #     user = User(email=email,
    #                 name=name,
    #                 gender=gender,
    #                 picture=picture,
    #                 is_active=is_active,
    #                 is_admin=is_admin)
    #     user.set_password(password)
    #     user.save()
    #     return user


class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'picture', 'gender']
        # exclude = ['created_at', 'otp', 'is_active', 'is_admin']
        extra_kwargs = {
            'picture': {'required': False},
            "gender": {'required': False}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'],
                                        name=validated_data['name'],
                                        password=validated_data['password'],
                                        password2=validated_data['password2'])
        return user

class UserResetChangePasswordSerializer(serializers.Serializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    # class Meta:
    #     model = User
    #     fields = ['password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs


class SpecificUserSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['email', 'name', 'gender', 'picture', 'is_active', 'is_admin', 'created_at']
        # exclude = ['password', 'otp']

