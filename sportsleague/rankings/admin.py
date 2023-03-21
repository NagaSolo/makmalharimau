from django.contrib import admin

from .models import File, Team, Game, GamePoint
# Register your models here.
admin.site.register(File)
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(GamePoint)