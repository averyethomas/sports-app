from django.contrib import admin
from sportsApp.models import Athlete, Team, Event

class AthleteAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(Athlete, AthleteAdmin)


class EventAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(Event, EventAdmin)


class TeamAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(Team, TeamAdmin)
