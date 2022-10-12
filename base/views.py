from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Room, Topic, Message
from .form import RoomForm

# Create your views here.

def index(request):

    if request.GET.get('q') != None:
        q = request.GET.get('q')
    else:
        q = ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    topics = Topic.objects.all()
    room_count = rooms.count()

    comments = Message.objects.filter(Q(room__topic__name__icontains=q))

    return render(request, "base/index.html", {'rooms': rooms,
                                               'topics': topics,
                                               'room_count': room_count,
                                               'comments': comments})


def forum (request, pk):

    room = Room.objects.get(id=pk)
    #comments = room.message_set.all().order_by('-created') #get all info from child table (message model) related to this room
    comments = Message.objects.filter(room=room) #get all info from child table (message model) related to this room
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST['body']
        )
        room.participants.add(request.user)
        return redirect('forum', pk=room.id)

    return render(request, "base/room.html", {'room': room,
                                              'comments':comments,
                                              'participants': participants})


def user_profile(request, pk):
    user = User.objects.get(id=pk)
    rooms = Room.objects.filter(host=user)
    comments = Message.objects.filter(user=user)
    topics = Topic.objects.all()
    return render(request, "base/profile.html", {'user': user,
                                                 'rooms': rooms,
                                                 'comments': comments,
                                                 'topics': topics})


#require authentication to use the method
@login_required(login_url='/accounts/login/')
def create_room (request):

    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, "base/room_form.html", {'form': form})

#require authentication to use the method
@login_required(login_url='/accounts/login/')
def update_room(request, pk):

    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    #check if the creator of the group is the one changing stuffs
    if request.user != room.host:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'base/room_form.html', {'form': form})

#require authentication to use the method
@login_required(login_url='/accounts/login/')
def delete_room(request, pk):

    room = Room.objects.get(id=pk)

    #check if the creator of the group is the one changing stuffs
    if request.user != room.host:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        room.delete()
        return redirect('index')

    return render(request, 'base/delete.html', {'obj': room})


#require authentication to use the method
@login_required(login_url='/accounts/login/')
def delete_message(request, pk):

    message = Message.objects.get(id=pk)

    #check if the creator of the group is the one changing stuffs
    if request.user != message.user:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        message.delete()
        return redirect('index')

    return render(request, 'base/delete.html', {'obj': message})


