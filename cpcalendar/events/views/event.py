from django.shortcuts import render, get_object_or_404, redirect
from ..models.events import Event
from ..forms import EventForm
import json
from django.urls import reverse

def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

def event_edit(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})

def event_delete(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
        return redirect('homepage')
    return render(request, 'events/event_confirm_delete.html', {'event': event})