from rest_framework import serializers
import re

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['email', 'password']

class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'cin', 'number', 'picture', 'address', 'birthdate', 'gender', 'is_active', 'is_admin']
        # exclude = ['created_at', 'otp', 'is_active', 'is_admin']
        # extra_kwargs = {
        #     'picture': {'required': False}
        # }

    def save(self):
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        name = self.validated_data['name']
        cin = self.validated_data['cin']
        address = self.validated_data['address']
        number = self.validated_data['number']
        gender = self.validated_data['gender']
        birthdate = self.validated_data['birthdate']
        picture = self.validated_data.get('picture', 'user.png')
        is_active = self.validated_data['is_active']
        is_admin = self.validated_data['is_admin']

        if not bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)):
            raise serializers.ValidationError({'message': 'Invalid email format!'})

        if password != password2 :
            raise serializers.ValidationError({'message': 'password mismatch!'})

        if not bool(re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$", password)):
            raise serializers.ValidationError({'message': 'password must contain least one digit, one uppercase letter, '
                                                          'at least one lowercase letter, at least one special character'})

        if len(name) == 0:
            raise serializers.ValidationError({'message': 'name should not be empty!'})
        # print(bool(re.match(r'^(?:\d{8}|\d{12})$', cin)))

        if not bool(re.match(r'^(?:\d{8}|\d{12})$', cin)):
            raise serializers.ValidationError({'message': 'cin is not correct!'})

        user = User(email=email,
                    name=name,
                    cin=cin,
                    gender=gender,
                    number=number,
                    address=address,
                    picture=picture,
                    birthdate=birthdate,
                    is_active=is_active,
                    is_admin=is_admin)
        user.set_password(password)
        user.save()
        return user
