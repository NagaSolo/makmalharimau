from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Game, Team, GamePoint, File

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='harimau', password='hentam')
        User.objects.create(username='singa', password='keromo')

    def test_user_is_created(self):
        harimau = User.objects.get(username='harimau', password='hentam')
        singa = User.objects.get(username='singa', password='keromo')
        self.assertEqual(harimau.username,'harimau')
        self.assertEqual(singa.username,'singa')


class FileTestCase(TestCase):
    # testing File model with status Failed or Success
    def setUp(self):
        File.objects.create(filename='fantasy_league_1.csv', status=True)
        File.objects.create(filename='fantasy_league_1.xlsx')

    def test_file_reference(self):
        success = File.objects.get(filename='fantasy_league_1.csv')
        failed = File.objects.get(filename='fantasy_league_1.xlsx')
        self.assertTrue(success.status,True)
        self.assertFalse(failed.status,True)


class RankingTestCase(TestCase):
    # testing team creation, game creation, and point award
    def setUp(self):
        crazy = Team.objects.create(name='Crazy Ones')
        rebs = Team.objects.create(name='Rebels')

        Game.objects.create(team_1=crazy, team_2=rebs)
        Game.objects.create(team_1=rebs, team_2=crazy)

    def test_team_is_created(self):
        team_1 = Team.objects.get(name='Crazy Ones')
        team_2 = Team.objects.get(name='Rebels')
        self.assertEqual(team_1.name,'Crazy Ones')
        self.assertEqual(team_2.name,'Rebels')

    def test_game_creation(self):
        crazy = Team.objects.get(name='Crazy Ones')
        rebs = Team.objects.get(name='Rebels')

        game_1 = Game.objects.get(team_1=crazy, team_2=rebs)
        game_2 = Game.objects.get(team_1=rebs, team_2=crazy)

        self.assertEqual(game_1.team_1.name,'Crazy Ones')
        self.assertEqual(game_1.team_2.name,'Rebels')
        self.assertEqual(game_2.team_1.name,'Rebels')
        self.assertEqual(game_2.team_2.name,'Crazy Ones')

    def test_point_award(self):
        crazy = Team.objects.get(name='Crazy Ones')
        rebs = Team.objects.get(name='Rebels')

        game_1 = Game.objects.get(team_1=crazy, team_2=rebs)
        game_2 = Game.objects.get(team_1=rebs, team_2=crazy)

        game1_team1_point = GamePoint.objects.create(game=game_1, team=crazy, point=3)
        game1_team2_point = GamePoint.objects.create(game=game_1, team=rebs, point=0)

        game2_team1_point = GamePoint.objects.create(game=game_2, team=rebs, point=0)
        game2_team2_point = GamePoint.objects.create(game=game_2, team=crazy, point=3)
        
        self.assertEqual(game1_team1_point.point,3)
        self.assertEqual(game1_team2_point.point,0)
        self.assertEqual(game2_team1_point.point,0)
        self.assertEqual(game2_team2_point.point,3)

        self.assertEqual(crazy.points_count(), 6)
        self.assertEqual(rebs.points_count(), 0)