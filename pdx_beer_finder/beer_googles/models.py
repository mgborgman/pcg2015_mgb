
from django.db import models
from django.contrib.auth.models import User


class Beer(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(unique=True, default='')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Beer"
        verbose_name_plural = "Beers"


class Bar(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    beers = models.ManyToManyField(Beer, related_name='bars')
    slug = models.SlugField(unique=True, default='')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Bar"
        verbose_name_plural = "Bars"


class BarRating(models.Model):
    rating = models.IntegerField()
    bar = models.ForeignKey(Bar)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return unicode(self.user)


class BeerRating(models.Model):
    rating = models.IntegerField(default=0)
    comment = models.TextField()
    beer = models.ForeignKey(Beer)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return unicode(self.user)


class BarComment(models.Model):
    comment = models.TextField()
    bar = models.ForeignKey(Bar)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return unicode(self.user)


class BeerComment(models.Model):
    Comment = models.TextField()
    bar = models.ForeignKey(Bar)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return unicode(self.user)


class UserProfile(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.user.username


