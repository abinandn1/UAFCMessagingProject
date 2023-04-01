from django.shortcuts import render, redirect
from messaging.models import Room, Message

# Create your views here.
def home(request):
    return render(request, 'home.html')


# Create your views here.
def room(request, room):
    return render(request, 'room.html')


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?username=') 
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/' + room + '/?username=') 