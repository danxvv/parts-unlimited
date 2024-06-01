from django.core.management.base import BaseCommand
from parts_unlimited.models import Part


class Command(BaseCommand):
    help = 'Clean the database; WARNING: This will delete all the data!'

    def handle(self, *args, **options):
        Part.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Data cleaned successfully!'))