from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView
from api.serializers import TournamentSerializer, RegisterSerializer, UserSerializer
from api.models import Tournament
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken

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

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })



class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)