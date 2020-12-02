from django.contrib import admin
from .models import About, HowTo, Project


for obj in [About, HowTo, Project]:
    admin.site.register(obj)
