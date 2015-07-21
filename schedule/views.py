from django.shortcuts import render, get_object_or_404
import time
from .models import Event
from django.contrib import messages
from .forms import EventForm, UpdateEventForm, LoginForm
from datetime import date
import calendar
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


mnames = [_("January"), _("February"), _("March"), _("April"), _("May"), _("June"), _("July"), _("August"), _("September"), _("October"), _("November"), _("December")]
cal = calendar.Calendar()


def index(request):
    if request.user.is_anonymous():
        return render(request, "index2.html")
    else:
        lst = [[]]
        lstlab = [[]]
        lstexams = [[]]
        lstceremony = [[]]
        week = 0
        nyear, nmonth = time.localtime()[:2]
        month_days = cal.itermonthdays(nyear, nmonth)
        for day in month_days:
            events = Event.objects.filter(
                date__year=nyear, date__month=nmonth, date__day=day)
            eventslab = events.filter(event_type=1)
            eventsexams = events.filter(event_type=0)
            eventsceremony = events.filter(event_type=2)
            lst[week].append((day, events))
            lstlab[week].append((day, eventslab))
            lstexams[week].append((day, eventsexams))
            lstceremony[week].append((day, eventsceremony))
            if len(lst[week]) == 7:
                lst.append([])
                lstlab.append([])
                lstexams.append([])
                lstceremony.append([])
                week += 1

        return render(request, "index.html", dict(
            weeks=lst,
            weekslab=lstlab,
            weeksexams=lstexams,
            weeksceremony=lstceremony,
            monthnumb=nmonth,
            nmonth=mnames[nmonth-1],
            nyear=int(nyear)))


def month(request, month, year, change):
    lst = [[]]
    lstlab = [[]]
    lstexams = [[]]
    lstceremony = [[]]
    week = 0
    monthnumb = int(month)

    if change == "prev":
        if monthnumb == 1:
            monthnumb = 12
            year = int(year) - 1
        else:
            monthnumb = monthnumb - 1
        month_days = cal.itermonthdays(int(year), monthnumb)
    else:
        if monthnumb == 12:
            monthnumb = 1
            year = int(year) + 1
        else:
            monthnumb = monthnumb + 1
        month_days = cal.itermonthdays(int(year), monthnumb)
    for day in month_days:
        events = Event.objects.filter(
            date__year=year, date__month=monthnumb, date__day=day)
        eventslab = events.filter(event_type=1)
        eventsexams = events.filter(event_type=0)
        eventsceremony = events.filter(event_type=2)
        lst[week].append((day, events))
        lstlab[week].append((day, eventslab))
        lstexams[week].append((day, eventsexams))
        lstceremony[week].append((day, eventsceremony))
        if len(lst[week]) == 7:
            lst.append([])
            lstlab.append([])
            lstexams.append([])
            lstceremony.append([])
            week += 1

    return render(request, "month.html", dict(
        weeks=lst,
        weekslab=lstlab,
        weeksexams=lstexams,
        weeksceremony=lstceremony,
        monthnumb=monthnumb,
        nmonth=mnames[monthnumb-1],
        nyear=int(year)))


def create_event(request, day, month, year):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.date = date(int(year), int(mnames.index(month)+1), int(day))
            event.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.add_message(
                    request, messages.INFO,
                    (_("Please fill in the blanks")))
            return HttpResponseRedirect(reverse(
                    'create_event', args=[day, month, year]))
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})


def update_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.POST:
        form = UpdateEventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.add_message(
                    request, messages.INFO,
                    (_("Please fill in the blanks")))
            return HttpResponseRedirect(reverse(
                    'update_event', args=[event.id]))
    else:
        form = UpdateEventForm(instance=event)
    return render(request, 'update_event.html', {'form': form, 'event': event})


def detail_day(request, day, month, year):
    events = Event.objects.filter(
        date=date(int(year), int(mnames.index(month)+1), int(day)))
    return render(
        request,
        'detail_day.html',
        {"events": events, "date": " ".join([day, month, year])})


def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    event.delete()
    return HttpResponseRedirect(reverse('index'))


def my_events(request):
    events = Event.objects.filter(user=request.user)
    return render(request, 'myevents.html', {"events": events})
