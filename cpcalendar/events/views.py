from django.shortcuts import render, get_object_or_404, redirect
from .models.events import Event
from .forms import EventForm
import json
from django.urls import reverse


def homepage(request):
    events = Event.objects.all()
    events_list = [{
        'id': event.id,
        'title': event.title,
        'start': event.date.strftime('%Y-%m-%d %H:%M:%S'),
        'description': event.description,
        'link': event.link,
        'url': reverse('event_detail', args=[event.id]),
    } for event in events]
    
    events_json = json.dumps(events_list)

    # Debug : afficher dans la console serveur les événements
    print("JSON des événements: efefe", events_json)  

    return render(request, 'homepage.html', {
        'events': events,
        'events_json': events_json
    })

def event_list(request):
    events = Event.objects.all()
    
    # Préparation du JSON pour le calendrier
    events_list = [{
        'id': event.id,
        'title': event.title,
        'start': event.date.strftime('%Y-%m-%d %H:%M:%S'),
        'description': event.description,
    } for event in events]
    
    events_json = json.dumps(events_list)

    # Debug pour s'assurer que le JSON est correct
    print("JSON des événements: fefe", events_json)

    # Envoie à la fois les événements pour la liste et le JSON pour le calendrier
    return render(request, 'events/event_list.html', {
        'events': events,
        'events_json': events_json
    })

def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

def event_edit(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})

def event_delete(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})


# Create your views here.
