from django.db.models import fields
from rest_framework import serializers
from .models import Tournament

class TournamentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tournament
		fields = ('tournamentname', 'venuename', 'startdate')
