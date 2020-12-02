from .models import About, HowTo, Project
from rest_framework import viewsets, views
from .serializers import AboutSerializer, HowToSerializer, ProjectSerializer
from rest_framework.response import Response


class AboutViewSet(viewsets.ModelViewSet):
    """ API Endpoint that retrieves the about statements """
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class HowToViewSet(viewsets.ModelViewSet):
    queryset = HowTo.objects.all()
    serializer_class = HowToSerializer

class ProjectView(views.APIView):
    def get(self, request, format=None):
        query = Project.objects.all()
        serializer = ProjectSerializer(query, many=True)
        return Response(serializer.data)
