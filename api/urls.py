from django.contrib import admin
from django.urls import path
from . import views

# urlpatterns = [
# 	path('', views.ApiOverview, name='home'),
# 	path('createtournament/', views.add_tournaments, name='add-tournaments'),
# 	path('getalltournaments/', views.view_tournaments, name='view_tournaments'),
# 	path('updatetournament/<int:pk>/', views.update_tournament, name='update-tournaments'),
# 	path('updatetournament/<int:pk>/delete/', views.delete_tournament, name='delete-items'),
# ]
urlpatterns = [
    path("alltournament/",views.ListAPIView.as_view(),name="tournament_list"),
    path("create/", views.CreateTournamentAPIView.as_view(),name="tournament_create"),
    path("update/<int:pk>/",views.UpdateTournamentAPIView.as_view(),name="update_tournament"),
    path("delete/<int:pk>/",views.DeleteTournamentAPIView.as_view(),name="delete_tournament")
]
