# Generated by Django 4.0.5 on 2022-07-01 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events_api', '0002_event_employeeitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='employeeitem',
        ),
    ]
