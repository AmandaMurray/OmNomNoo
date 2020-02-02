from django.db import models
from django.conf import settings
settings.configure(DEBUG=True)

class Restaurant(models.Model):
    name = models.CharField()
    currScore = models.IntegerField(default = 0)
