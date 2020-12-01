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
