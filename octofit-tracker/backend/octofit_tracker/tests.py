from django.test import TestCase
from .models import Team, User, Activity, Leaderboard, Workout

class TeamTestCase(TestCase):
    def setUp(self):
        Team.objects.create(name="Marvel")

    def test_team_creation(self):
        marvel = Team.objects.get(name="Marvel")
        self.assertEqual(marvel.name, "Marvel")

class UserTestCase(TestCase):
    def setUp(self):
        team = Team.objects.create(name="DC")
        User.objects.create(name="Batman", email="batman@dc.com", team=team)

    def test_user_creation(self):
        batman = User.objects.get(email="batman@dc.com")
        self.assertEqual(batman.name, "Batman")

class ActivityTestCase(TestCase):
    def setUp(self):
        team = Team.objects.create(name="Marvel")
        user = User.objects.create(name="Iron Man", email="ironman@marvel.com", team=team)
        Activity.objects.create(user=user, type="Run", duration=30, distance=5.0)

    def test_activity_creation(self):
        activity = Activity.objects.get(type="Run")
        self.assertEqual(activity.duration, 30)

class LeaderboardTestCase(TestCase):
    def setUp(self):
        team = Team.objects.create(name="DC")
        user = User.objects.create(name="Superman", email="superman@dc.com", team=team)
        Leaderboard.objects.create(user=user, points=100)

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.get(points=100)
        self.assertEqual(lb.user.name, "Superman")

class WorkoutTestCase(TestCase):
    def setUp(self):
        team = Team.objects.create(name="Marvel")
        user = User.objects.create(name="Captain America", email="cap@marvel.com", team=team)
        Workout.objects.create(user=user, name="Chest Day", description="Bench press")

    def test_workout_creation(self):
        workout = Workout.objects.get(name="Chest Day")
        self.assertEqual(workout.description, "Bench press")