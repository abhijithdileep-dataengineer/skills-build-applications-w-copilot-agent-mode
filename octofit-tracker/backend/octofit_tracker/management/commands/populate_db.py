from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        for model in [Leaderboard, Activity, Workout, User, Team]:
            try:
                model.objects.all().delete()
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Could not delete {model.__name__}: {e}"))

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        tony = User.objects.create(email='tony@stark.com', username='IronMan', team=marvel)
        steve = User.objects.create(email='steve@rogers.com', username='CaptainAmerica', team=marvel)
        bruce = User.objects.create(email='bruce@wayne.com', username='Batman', team=dc)
        clark = User.objects.create(email='clark@kent.com', username='Superman', team=dc)

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        pushups = Workout.objects.create(name='Pushups', description='Upper body workout')
        running = Workout.objects.create(name='Running', description='Cardio workout')
        pushups.suggested_for.set([tony, bruce])
        running.suggested_for.set([steve, clark])

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(user=tony, activity_type='Pushups', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, activity_type='Running', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, activity_type='Pushups', duration=25, date=timezone.now().date())
        Activity.objects.create(user=clark, activity_type='Running', duration=50, date=timezone.now().date())

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(user=tony, score=100, rank=1)
        Leaderboard.objects.create(user=steve, score=90, rank=2)
        Leaderboard.objects.create(user=bruce, score=80, rank=3)
        Leaderboard.objects.create(user=clark, score=70, rank=4)

        self.stdout.write(self.style.SUCCESS('Test data created successfully!'))
