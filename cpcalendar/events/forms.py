from django import forms
from .models.events import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'type', 'link', 'is_recurring', 'recurrence_rule']