from django import forms
from .models import Event
from django.utils.translation import ugettext as _


class LoginForm(forms.Form):
    username = forms.CharField(label=_("Username"))
    password = forms.CharField(label=_("password"), widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError(_("Username or password is wrong"))


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ["user", "date", "decline"]


class UpdateEventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ["user", "date", "decline"]
