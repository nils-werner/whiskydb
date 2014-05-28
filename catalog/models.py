from django.db import models


class Variety(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class Distillery(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

class Whisky(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    variety = models.ForeignKey(Variety)
    distillery = models.ForeignKey(Distillery)

    def __unicode__(self):
        return self.name
