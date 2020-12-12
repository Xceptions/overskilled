from django.contrib import admin
from .models import About, HowTo, Project, Competition


for obj in [About, HowTo, Project, Competition]:
    admin.site.register(obj)
