from django.shortcuts import render, get_object_or_404, redirect
from ..models.events import Event
from ..forms import EventForm
import json
from django.urls import reverse

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