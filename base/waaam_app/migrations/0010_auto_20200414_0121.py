# Generated by Django 3.0.3 on 2020-04-14 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waaam_app', '0009_auto_20200309_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerrecord',
            name='activity',
            field=models.CharField(choices=[('Maintenance', 'Maintenance'), ('Administration', 'Administration'), ('Outreach', 'Outreach'), ('Education', 'Education')], max_length=256),
        ),
    ]
