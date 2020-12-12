from django.db import models

class About(models.Model):
    the_short = models.CharField(max_length=200)
    the_long = models.TextField()

    def __str__(self):
        return self.the_short

class HowTo(models.Model):
    ace_comp = models.TextField()
    ace_comp_res = models.TextField()
    get_proj = models.TextField()
    get_proj_res = models.TextField()
    get_jobs = models.TextField()
    get_jobs_res = models.TextField()

    def __str__(self):
        return self.ace_comp

class Project(models.Model):
    BARGAIN_CHOICES = (
        ('negotiable', 'NEGOTIABLE'),
        ('fixed', 'FIXED')
    )
    project_header = models.CharField(max_length=200, default='Project for a Techie')
    project_body = models.TextField()
    amount = models.CharField(max_length=100, default='100')
    bargain = models.CharField(max_length=20, choices=BARGAIN_CHOICES, default='negotiable')
    location = models.TextField()
    contact_me = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.project_header

class Jobs(models.Model):
    title = models.CharField(max_length=200)
    company = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title