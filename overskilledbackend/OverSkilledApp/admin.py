from django.contrib import admin
from .models import About, HowTo, Project, Jobs


for obj in [About, HowTo, Project, Jobs]:
    admin.site.register(obj)
