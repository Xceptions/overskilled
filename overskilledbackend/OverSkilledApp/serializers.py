from .models import About, HowTo
from rest_framework import serializers


class AboutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = About
        fields = ['the_short', 'the_long']

class HowToSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HowTo
        fields = '__all__'