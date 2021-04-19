from rest_framework import serializers
from .models import Jordan, Puma, Nike
from djoser.serializers import UserCreateSerializer, UserSerializer
from . import models

class UserCreateSerializer(UserCreateSerializer):
    
    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'username', 'password', 'avatar')

class JordanSerializer(serializers.HyperlinkedModelSerializer):
    
    jordan_url = serializers.ModelSerializer.serializer_url_field(
        view_name='jordan_detail',
    )

    class Meta: 
        model = Jordan
        fields = ('id', 'image_url', 'name', 'price', 'jordan_url')


class PumaSerializer(serializers.HyperlinkedModelSerializer):
    
    puma_url = serializers.ModelSerializer.serializer_url_field(
        view_name='puma_detail',
    )

    class Meta:
        model = Puma
        fields = ('id', 'image_url', 'name', 'price', 'puma_url')


class NikeSerializer(serializers.HyperlinkedModelSerializer):
    
    nike_url = serializers.ModelSerializer.serializer_url_field(
        view_name='nike_detail',
    )

    class Meta:
        model = Nike
        fields = ('id', 'image_url', 'name', 'price', 'nike_url')
