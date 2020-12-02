from .models import About, HowTo, Project
from rest_framework import serializers


class AboutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = About
        fields = ['the_short', 'the_long']

class HowToSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HowTo
        fields = '__all__'

class ProjectSerializer(serializers.Serializer):
    project_header = serializers.CharField()
    project_body = serializers.CharField()
    amount = serializers.CharField()
    bargain = serializers.CharField()
    location = serializers.CharField()
    contact_me = serializers.CharField()