from django.contrib import admin
from .models import About, HowTo, Project, Competition, Subscribers, ContactUs


for obj in [About, HowTo, Project, Competition, Subscribers, ContactUs]:
    admin.site.register(obj)
