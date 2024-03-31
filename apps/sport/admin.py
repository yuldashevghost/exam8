from django.contrib import admin

from apps.sport.models import Sport, Chempionship, Team, Match, Rating


# Register your models here.
@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    pass

@admin.register(Chempionship)
class ChempionshipAdmin(admin.ModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass