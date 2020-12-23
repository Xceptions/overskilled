from django.contrib import admin
from .models import About, HowTo, Project, Job, Competition, Subscribers, ContactUs


for obj in [About, HowTo, Project, Competition, Subscribers, ContactUs, Job]:
    admin.site.register(obj)
