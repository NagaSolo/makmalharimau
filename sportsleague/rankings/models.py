
from django.db import models

# Create your models here.

class File(models.Model):
    filename = models.CharField(max_length=128)
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


class Team(models.Model):
    name = models.CharField(max_length=32)

    def points_count(self):
        overall_points = 0
        gamepoints = GamePoint.objects.select_related('team').filter(team__name__iexact=self.name)
        for gamepoint in gamepoints:
            overall_points += gamepoint.point
        return overall_points
        

class Game(models.Model):
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_1")
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_2")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.team_1.name + ' vs ' + self.team_2.name + ' at ' + self.timestamp.astimezone


class GamePoint(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team")
    point = models.IntegerField(blank=True, null=True)