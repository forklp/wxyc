from django.core.management.base import BaseCommand, CommandError
from appoint_car import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = models.User.objects.all()
        print(users[0].name)
