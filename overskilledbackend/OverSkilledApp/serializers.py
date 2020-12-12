from .models import About, HowTo, Project, Jobs
from rest_framework import serializers


class AboutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = About
        fields = ['the_short', 'the_long']

class HowToSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HowTo
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'