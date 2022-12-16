from django.forms import ModelForm
from .models import Room, User

#from django.contrib.auth.models import User, auth

#create a model based form

'''

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

'''


class RoomForm(ModelForm):
    class Meta:
        model = Room           #reference the model
        fields = '__all__'     #select all the fields
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username', 'email','bio']

