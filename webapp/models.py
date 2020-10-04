from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import calendar
from datetime import date, time, timedelta

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    
    def __str__(self):
        return "{}".format(self.username)

class Tag(models.Model):
    title = models.CharField(max_length=100, null=True, blank=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return "{}".format(self.title)

class WardrobePost(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    customer = models.ForeignKey(Customer, related_name="wardrobepost_set", on_delete=models.CASCADE,blank=True, null=True)
    caption = models.TextField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # imagee = models.ImageField()
    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return "{}".format(self.title)
