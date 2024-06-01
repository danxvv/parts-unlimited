import random
import string
from django.core.management.base import BaseCommand
from parts_unlimited.models import Part
from faker import Faker


class Command(BaseCommand):
    help = 'Fill the database with fake data'

    def add_arguments(self, parser):
        parser.add_argument('number_of_parts', type=int)

    def handle(self, *args, **options):
        fake = Faker(['en_US'])
        number_of_parts = options['number_of_parts']

        parts = []
        for _ in range(number_of_parts):
            sku = ''.join(random.choices(string.ascii_letters + string.digits, k=13))
            parts.append(Part(
                name=fake.name(),
                sku=sku,
                description=fake.text(max_nb_chars=1000),
                weight_ounces=fake.random_int(min=1, max=100),
                is_active=fake.boolean()
            ))

        Part.objects.bulk_create(parts)
        self.stdout.write(self.style.SUCCESS('Data filled successfully!'))
