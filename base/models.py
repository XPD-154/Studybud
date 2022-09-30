from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)    #refernce key in another table
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)  #don't delete the reference key
    name = models.CharField(max_length=200)                                 #stands for VARCHAR
    description = models.TextField(null=True, blank=True)                   #stands for textfield
    # participants =
    updated = models.DateTimeField(auto_now=True)                           #DateTime field auto stamped
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']                                 #order table in reverse order(-)

    def __str__(self):                                                      #The __str__ function is used add a
        return self.name                                                    #string representation of a model's object

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)                #delete once reference is deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
