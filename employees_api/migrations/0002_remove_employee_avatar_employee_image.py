# Generated by Django 4.0.5 on 2022-06-30 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='avatar',
        ),
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]