# from PIL import Image, ImageDraw, ImageFont
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'first_name', 'last_name', 'sex')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Password fields didn\'t match.'})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            sex=validated_data['sex']
        )

        user.set_password(validated_data['password'])
        user.save()

        # photo = Image.open(validated_data['avatar'])
        # drawing = ImageDraw.Draw(photo)
        # black = (3, 8, 12)
        # font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
        # drawing.text((5, 5), 'watermark', fill=black, font=font)
        # photo.save(output_image_path)

        return user
