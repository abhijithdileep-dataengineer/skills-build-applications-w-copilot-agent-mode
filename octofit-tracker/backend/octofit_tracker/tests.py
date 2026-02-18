from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.user = User.objects.create(email='tony@stark.com', username='IronMan', team=self.team)
        self.workout = Workout.objects.create(name='Pushups', description='Upper body workout')
        self.activity = Activity.objects.create(user=self.user, activity_type='Running', duration=30, date='2024-01-01')
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100, rank=1)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Marvel')
    def test_user_str(self):
        self.assertEqual(str(self.user), 'IronMan')
    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Pushups')
    def test_activity_str(self):
        self.assertEqual(str(self.activity), 'IronMan - Running')
    def test_leaderboard_str(self):
        self.assertEqual(str(self.leaderboard), 'IronMan - 100')
