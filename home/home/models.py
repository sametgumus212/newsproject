from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    link=models.CharField('Venue Name',max_length=200)
    def __str__(self):
        return self.link