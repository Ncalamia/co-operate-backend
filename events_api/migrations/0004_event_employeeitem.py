# Generated by Django 4.0.5 on 2022-07-01 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employeeitem_api', '0003_remove_employeeitem_event'),
        ('events_api', '0003_remove_event_employeeitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='employeeitem',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='employeeitem_api.employeeitem'),
        ),
    ]
