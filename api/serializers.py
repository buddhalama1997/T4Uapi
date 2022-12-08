from django.db.models import fields
from rest_framework import serializers
from .models import Tournament
from django.contrib.auth.models import User


class TournamentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tournament
		fields = ('tournamentname', 'venuename', 'startdate')


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user
