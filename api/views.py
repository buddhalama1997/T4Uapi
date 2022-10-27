from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView
from api.serializers import TournamentSerializer
from api.models import Tournament

# to view all the tournament
class ListTounamentAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

# to create all the tournament
class CreateTournamentAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
# to update all the tournament
class UpdateTournamentAPIView(RetrieveUpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
# to delete
class DeleteTournamentAPIView(RetrieveDestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer