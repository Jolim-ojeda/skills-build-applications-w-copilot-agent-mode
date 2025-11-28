from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Avengers', universe='Marvel')
        self.user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=self.team)
        self.workout = Workout.objects.create(name='Pushups', description='Do 50 pushups', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, date='2025-11-28')
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100, rank=1)

    def test_team(self):
        self.assertEqual(self.team.name, 'Avengers')

    def test_user(self):
        self.assertEqual(self.user.email, 'ironman@marvel.com')

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Pushups')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'Running')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.rank, 1)
