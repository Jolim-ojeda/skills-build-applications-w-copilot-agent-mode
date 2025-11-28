from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data in dependency order (children before parents)
        for obj in Leaderboard.objects.all():
            if obj.id:
                obj.delete()
        for obj in Activity.objects.all():
            if obj.id:
                obj.delete()
        for obj in User.objects.all():
            if obj.id:
                obj.delete()
        for obj in Team.objects.all():
            if obj.id:
                obj.delete()
        for obj in Workout.objects.all():
            if obj.id:
                obj.delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', universe='Marvel')
        dc = Team.objects.create(name='DC', universe='DC')

        # Create Users (Super Heroes)
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Pushups', description='Do 50 pushups', difficulty='Easy'),
            Workout.objects.create(name='Running', description='Run 5km', difficulty='Medium'),
            Workout.objects.create(name='Deadlift', description='Deadlift 100kg', difficulty='Hard'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date=date.today())
        Activity.objects.create(user=users[1], type='Pushups', duration=15, date=date.today())
        Activity.objects.create(user=users[3], type='Deadlift', duration=45, date=date.today())

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=150, rank=1)
        Leaderboard.objects.create(user=users[1], score=120, rank=2)
        Leaderboard.objects.create(user=users[3], score=100, rank=3)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
