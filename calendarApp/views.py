from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django import forms

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


from .models import Choice, Question, Events

from django.utils import timezone

from .forms import AddEventForm, RegisterForm


def eventView(request):
    eventId = request.GET.get('eventId')

    if eventId is None:
        return 404
    else:
        event = Events.objects.get(pk=eventId)
        return render(request, 'calendarApp/viewEvent.html', {
            'event': event,
        })

def event(request):
    all_events = Events.objects.all()
    # if filters applied then get parameter and filter based on condition else return object
    if request.GET:
        event_arr = []

        for i in all_events:
            event_sub_arr = {}
            event_sub_arr['title'] = i.title
            start_date = datetime.datetime.strptime(str(i.start.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            end_date = datetime.datetime.strptime(str(i.end.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            event_sub_arr['start'] = start_date
            event_sub_arr['end'] = end_date
            event_arr.append(event_sub_arr)
        return HttpResponse(json.dumps(event_arr))

    context = {
        "events":all_events,

    }
    return render(request,'calendarApp/calendar.html',context)

class HomeView(generic.ListView):
    template_name = 'calendarApp/home.html'

    def get_queryset(self):
      """Return the last five published questions."""
      return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

def LogoutView(request):
    logout(request)
    return render(request = request,
                  template_name = "calendarApp/home.html",)

class MessageView(generic.ListView):
    template_name = 'calendarApp/message.html'

    def get_queryset(self):
      """Return the last five published questions."""
      return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class IndexView(generic.ListView):
    template_name = 'calendarApp/index.html'

    def get_queryset(self):
      """Return the last five published questions."""
      return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

def addEventView(request):
     if request.method == "POST":
        form = AddEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('/', pk=event.pk)
     else:
        form = AddEventForm()
     return render(request, 'calendarApp/addEvent.html', {'form': form})

class ProfileView(generic.ListView):
    template_name = 'calendarApp/profile.html'

    def get_queryset(self):
      """Return the last five published questions."""
      return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

def RegisterView(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=User.objects.create_user(form.cleaned_data['username'], password=form.cleaned_data['password'])
            user.is_superuser=False
            user.is_staff=False
            user.save()
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'calendarApp/register.html', {'form': form})
