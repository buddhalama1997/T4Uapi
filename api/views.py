from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from api.serializers import TournamentSerializer
from api.models import Tournament

# Create your views here.
class ListAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

class CreateTournamentAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

class UpdateTournamentAPIView(RetrieveUpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

class DeleteTournamentAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer