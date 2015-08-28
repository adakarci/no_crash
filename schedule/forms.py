from django import forms
from .models import Event
from django.utils.translation import ugettext as _

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ["user", "date", "decline"]


class UpdateEventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ["user", "date", "decline"]
