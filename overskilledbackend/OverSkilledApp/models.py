from django.db import models

class About(models.Model):
    the_short = models.CharField(max_length=200)
    the_long = models.TextField()

    def __str__(self):
        return self.the_short
