from .models import About, HowTo, Project, Competition
from rest_framework import viewsets, views, status
from .serializers import AboutSerializer, HowToSerializer, ProjectSerializer, CompetitionSerializer
from rest_framework.response import Response
from django.http import Http404


class AboutViewSet(viewsets.ModelViewSet):
    """ API Endpoint that retrieves the about statements """
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class HowToViewSet(viewsets.ModelViewSet):
    queryset = HowTo.objects.all()
    serializer_class = HowToSerializer

class ProjectView(views.APIView):
    def get(self, request, format=None):
        query = Project.objects.all().order_by('-id')
        serializer = ProjectSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailsView(views.APIView):
    def get(self, request, project_id):
        query = Project.objects.get(pk=project_id)
        serializer = ProjectSerializer(query)
        return Response(serializer.data)


class CompetitionView(views.APIView):
    def get(self, request, format=None):
        query = Competition.objects.all().order_by('-id')
        serializer = CompetitionSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompetitionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)