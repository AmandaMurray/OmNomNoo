from django.db import models

class Restaurant(Models.model):
    name = models.charField()
    currScore = models.IntegerField(default = 0)
