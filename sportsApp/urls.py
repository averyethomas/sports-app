from django.conf.urls import patterns, url

from sportsApp  import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^events/$', views.event, name='sportsApp_course_list'),
    url(r'^rankings/$', views.ranking, name='sportsApp_athlete_list'),
    url(r'^rankings/(?P<pk>\d+)$', views.athlete, name='sportsApp_athlete'),
)
