from django.forms import ModelForm
from .models import Room

#create a model based form

class RoomForm(ModelForm):
    class Meta:
        model = Room           #reference the model
        fields = '__all__'     #select all the fields
        exclude = ['host', 'participants']
