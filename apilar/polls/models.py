
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    group = models.ForeignKey(Group, related_name='person', on_delete=models.PROTECT)

    def __str__(self):
        return self.first_name
