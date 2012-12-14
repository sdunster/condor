from django.db import models

class Rank(models.Model):
    code = models.CharField(
        max_length=3)
    name = models.CharField(
        max_length=64)

    def __unicode__(self):
        return name

class Qualification(models.Model):
    code = models.CharField(
        max_length=4)
    name = models.CharField(
        max_length=64)

    def __unicode__(self):
        return name

class Unit(models.Model):
    code = models.CharField(
        max_length=3)
    name = models.CharField(
        max_length=64)
    
    def __unicode__(self):
        return name

class Member(models.Model):
    id_number = models.IntegerField(
        max_length=8)
    surname = models.CharField(
        max_length=32)
    other_names = models.CharField(
        max_length=64)
    
    mobile = models.CharField(
        max_length=16)
    email = models.EmailField()
    
    rank = models.ForeignKey(Rank)
    qualifications = models.ManyToManyField(Qualification)
    
    def __unicode__(self):
        return "%s, %s" % (surname, other_names)


