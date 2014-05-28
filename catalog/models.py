from django.db import models


class Variety(models.Model):
    name = models.CharField(max_length=256)


class Distillery(models.Model):
    name = models.CharField(max_length=256)


class Whisky(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    variety = models.ForeignKey(Variety)
    distillery = models.ForeignKey(Distillery)
