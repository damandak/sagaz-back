# Generated by Django 4.0.4 on 2022-05-28 23:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sagazapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lake',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lake',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='lakemeasurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lakemeasurement',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
