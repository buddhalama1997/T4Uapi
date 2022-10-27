from django.db import models

class Tournament(models.Model):
	tournamentname = models.CharField(max_length=255)
	venuename = models.CharField(max_length=255)
	startdate = models.DateField()

	def __str__(self) -> str:
		return self.tournamentname
