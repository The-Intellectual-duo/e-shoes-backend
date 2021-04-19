from rest_framework import generics
from .serializers import JordanSerializer, PumaSerializer, NikeSerializer
from .models import Jordan, Puma, Nike

# Create your views here.
class JordanList(generics.ListCreateAPIView):
    queryset = Jordan.objects.all()
    serializer_class = JordanSerializer

class JordanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jordan.objects.all()
    serializer_class = JordanSerializer

class PumaList(generics.ListCreateAPIView):
    queryset = Puma.objects.all()
    serializer_class = PumaSerializer


class PumaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Puma.objects.all()
    serializer_class = PumaSerializer


class NikeList(generics.ListCreateAPIView):
    queryset = Nike.objects.all()
    serializer_class = NikeSerializer


class NikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nike.objects.all()
    serializer_class = NikeSerializer
