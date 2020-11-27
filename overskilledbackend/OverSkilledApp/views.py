from .models import About
from rest_framework import viewsets
from .serializers import AboutSerializer


class AboutViewSet(viewsets.ModelViewSet):
    """ API Endpoint that retrieves the about statements """
    queryset = About.objects.all()
    serializer_class = AboutSerializer
