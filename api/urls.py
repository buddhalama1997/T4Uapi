from django.contrib import admin
from django.urls import path
from . import views
from .views import RegisterAPI, LoginAPI
from knox import views as knox_views
# urlpatterns = [
# 	path('', views.ApiOverview, name='home'),
# 	path('createtournament/', views.add_tournaments, name='add-tournaments'),
# 	path('getalltournaments/', views.view_tournaments, name='view_tournaments'),
# 	path('updatetournament/<int:pk>/', views.update_tournament, name='update-tournaments'),
# 	path('updatetournament/<int:pk>/delete/', views.delete_tournament, name='delete-items'),
# ]
urlpatterns = [
    path("alltournament/",views.ListTounamentAPIView.as_view(),name="tournament_list"),
    path("create/", views.CreateTournamentAPIView.as_view(),name="tournament_create"),
    path("update/<int:pk>/",views.UpdateTournamentAPIView.as_view(),name="update_tournament"),
    path("delete/<int:pk>/",views.DeleteTournamentAPIView.as_view(),name="delete_tournament"),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
