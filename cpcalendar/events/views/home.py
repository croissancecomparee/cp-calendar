from django.shortcuts import render, get_object_or_404, redirect
from ..models.events import Event
from ..forms import EventForm
import json
from django.urls import reverse

def homepage(request):
    events = Event.objects.all()
    # events_list = [{
    #     'id': event.id,
    #     'title': event.title,
    #     'start': event.date.strftime('%Y-%m-%d %H:%M:%S'),
    #     'description': event.description,
    #     'link': event.link,
    #     'url': reverse('event_detail', args=[event.id]),
    # } for event in events]
    
    events_list = [{
        'id': event.id,
        'title': event.title,
        'start': event.date.strftime('%Y-%m-%d %H:%M:%S'),
        'description': event.description,
        'link': event.link,
        'type': event.type,
        'url': reverse('event_detail', args=[event.id]),
        'is_recurring': event.is_recurring,
        'recurrence_rule': event.recurrence_rule,
    } for event in events]

    events_json = json.dumps(events_list)

    # Debug : afficher dans la console serveur les événements
    print("JSON des événements: efefe", events_json)  

    return render(request, 'homepage.html', {
        'events': events,
        'events_json': events_json
    })