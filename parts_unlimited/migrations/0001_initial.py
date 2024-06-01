# Generated by Django 5.0.6 on 2024-05-31 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('sku', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1024)),
                ('weight_ounces', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
