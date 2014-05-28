from django.db import models


class User(models.Model):
    whiskies = models.ManyToManyField('catalog.Whisky', through='Purchase')


class Purchase(models.Model):
    user = models.ForeignKey(User)
    whisky = models.ForeignKey('catalog.Whisky')
    date = models.DateField()
    price = models.IntegerField()
