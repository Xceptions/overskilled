from .models import About, HowTo
from rest_framework import viewsets
from .serializers import AboutSerializer, HowToSerializer


class AboutViewSet(viewsets.ModelViewSet):
    """ API Endpoint that retrieves the about statements """
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class HowToViewSet(viewsets.ModelViewSet):
    queryset = HowTo.objects.all()
    serializer_class = HowToSerializer
