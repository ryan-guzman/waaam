# Generated by Django 2.2.6 on 2020-05-24 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waaam_app', '0016_auto_20200513_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='volunteer_waiver_and_release',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
