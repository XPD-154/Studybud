from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)    #refernce key in another table(auth_user)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)  #don't delete the reference key
    name = models.CharField(max_length=200)                                 #stands for VARCHAR
    description = models.TextField(null=True, blank=True)                   #stands for textfield
    participants = models.ManyToManyField(User, related_name='participants', blank=True) #'blank' means field can be left blank, change tag 'User' to 'participants' via related_name function
    updated = models.DateTimeField(auto_now=True)                           #DateTime field auto stamped
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']                                 #order table in reverse order(-)

    def __str__(self):                                                      #The only output if its referenced
        return self.name                                                    #anywhere without specific mention of any
                                                                            #column

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)                #picking the id of the 'user' creating a message. delete once reference is deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE)                #picking the id of the 'room' where message is created.
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]


