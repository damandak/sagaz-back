# Generated by Django 4.0.4 on 2022-06-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sagazapp', '0002_lake_created_at_lake_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lake',
            name='altitude',
            field=models.FloatField(blank=True, null=True, verbose_name='altitude (meters)'),
        ),
    ]