from django.shortcuts import render, redirect
from .models import Room, Topic
from .form import RoomForm

# Create your views here.

def index(request):

    if request.GET.get('q') != None:
        q = request.GET.get('q')
    else:
        q = ''

    rooms = Room.objects.filter(topic__name__icontains=q)

    topics = Topic.objects.all()

    return render(request, "base/index.html", {'rooms': rooms, 'topics': topics})

def forum (request, pk):

    room = Room.objects.get(id=pk)
    return render(request, "base/room.html", {'room': room})

def create_room (request):

    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, "base/room_form.html", {'form': form})

def update_room(request, pk):

    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'base/room_form.html', {'form': form})

def delete_room(request, pk):

    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('index')

    return render(request, 'base/delete.html', {'obj': room})
