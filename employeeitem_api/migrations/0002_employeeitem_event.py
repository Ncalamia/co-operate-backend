# Generated by Django 4.0.5 on 2022-07-01 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events_api', '0001_initial'),
        ('employeeitem_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeitem',
            name='event',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='events_api.event'),
        ),
    ]
