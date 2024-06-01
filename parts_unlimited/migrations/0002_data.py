from django.db import migrations, models
from parts_unlimited.models import Part

def create_default_data(apps, schema_editor):
    Part.objects.create(name='Heavy coil',
                        sku='SDJDDH8223DHJ',
                        description='Tightly wound nickel-gravy alloy spring',
                        weight_ounces=22,
                        is_active=1)
    Part.objects.create(name='Reverse lever',
                        sku='DCMM39823DSJD',
                        description='Attached to provide inverse leverage',
                        weight_ounces=9,
                        is_active=0)
    Part.objects.create(name='Macrochip',
                        sku='OWDD823011DJSD',
                        description='Used for heavy-load computing',
                        weight_ounces=2,
                        is_active=1)


class Migration(migrations.Migration):
    dependencies = [
        ('parts_unlimited', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_default_data),
    ]