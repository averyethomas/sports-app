# roster/views.py
from django.shortcuts import render
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
	event_list = Event.objects.all()
	return render(request, "sportsApp/events.html", {'events': event_list})

def ranking(request):
	athlete_list = Athlete.objects.all()
	return render(request, 'sportsApp/rankings.html', {'athletes': athlete_list})

def athlete(request):
	athlete = get_object_or_404(Athlete, id=pk)
	return render(request, 'sportsApp/athlete.htm', {'athlete': athlete})
	
