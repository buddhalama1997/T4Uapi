from django.contrib import admin
from .models import Tournament
# Register your models here.
# Register your models here.
@admin.register(Tournament)

class postModelAdmin(admin.ModelAdmin):
    list_display = ['id','tournamentname', 'venuename', 'startdate']