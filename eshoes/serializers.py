from rest_framework import serializers
from .models import Jordan, Puma, Nike

class JordanSerializer(serializers.HyperlinkedModelSerializer):

    class Meta: 
        model = Jordan
        fields = ('id', 'image_url', 'name', 'price',)


class PumaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Puma
        fields = ('id', 'image_url', 'name', 'price',)


class NikeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Nike
        fields = ('id', 'image_url', 'name', 'price',)
