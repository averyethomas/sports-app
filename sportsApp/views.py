# roster/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from sportsApp.models import Athlete, Team, Event

def home(request):
	context = {
		'athlete_count': Athlete.objects.count(),
		'event_count': Event.objects.count(),
		'team_count': Team.objects.count(),
	}
	return render(request, "sportsApp/home.html", context)

def event(request):
	mens_events = Event.objects.filter(gender="m")
	womens_events = Event.objects.filter(gender="f")
	return render(request, "sportsApp/events.html", {'mensevents': mens_events, 'womensevents': womens_events})

def ranking(request):
	athlete_list = Athlete.objects.all()
	womens_list = Athlete.objects.filter(team__name="WOMEN'S")
	mens_list = Athlete.objects.filter(team__name="MEN'S")
	return render(request, 'sportsApp/rankings.html', {'menslist': mens_list, 'womenslist': womens_list})

def athlete(request, pk):
	athlete = get_object_or_404(Athlete, id=pk)
	return render(request, 'sportsApp/athlete.html', {'athlete': athlete})
	
