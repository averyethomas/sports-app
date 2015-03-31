from django.db import models

# Create your models here.

class Athlete(models.Model):
	name = models.CharField(unique=True, max_length=50)
	team = models.ForeignKey("Team", null=True)
	rank = models.IntegerField(unique=False, max_length=2)
	points = models.IntegerField(unique=False, max_length=10)
	earnings = models.IntegerField(unique=False, max_length=15)
	jerseyNumber = models.IntegerField(unique=False, max_length=2)
	CTHeatWins = models.IntegerField(unique=False, max_length=10)
	avgHeatScore = models.CharField(unique=False, max_length=10)
	hometown = models.CharField(unique=False, max_length=100)
	country = models.CharField(unique=False, max_length=50)
	height= models.CharField(unique=False, max_length=6)
	weight = models.IntegerField(unique=False, max_length=3)
	dob = models.CharField(unique=False, max_length=10)
	winnings = models.CharField(unique=False, max_length=20)
	instagram = models.CharField(unique=True, max_length=20, blank=True)
	twitter = models.CharField(unique=True, max_length=20, blank=True)
	avatar = models.ImageField("avatars", blank=True, null=True)
	photo1 = models.ImageField("photos", blank=True, null=True)
	photo2 = models.ImageField("photos", blank=True, null=True)
	photo3 = models.ImageField("photos", blank=True, null=True)
	
	
	class Meta(object):
		verbose_name_plural = "Athletes"
		ordering = ('rank',)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.name = self.name.upper()
		super(Athlete, self).save(*args, **kwargs)


class Event(models.Model):
	name = models.CharField(unique=True, max_length=50)
	startdate = models.DateField();
	enddate = models.DateField();
	number = models.CharField(unique=True, max_length=2)
	champion = models.ForeignKey("Athlete", blank=True,  null=True, related_name="championevent")
	defendingchampion = models.ForeignKey("Athlete", blank= True, null=True, related_name="defendingchampionevent")
	location = models.CharField(unique=True, max_length=50)	
	team = models.ForeignKey("Team")


	class Meta(object):
		verbose_name_plural = "Events"
		ordering = ('number',)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.name = self.name.upper()
		super(Event, self).save(*args, **kwargs)




class Team(models.Model):
	name = models.CharField(unique=True, max_length=50)
	
	class Meta(object):
		verbose_name_plural = "Teams"
		ordering = ('name',)
	
	def __unicode__(self):
		return self.name
	
	def save(self, *args, **kwargs):
		self.name = self.name.upper()
		super(Team, self).save(*args, **kwargs)
