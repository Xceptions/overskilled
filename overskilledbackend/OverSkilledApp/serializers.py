from .models import About
from rest_framework import serializers


class AboutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = About
        fields = ['the_short', 'the_long']