# Generated by Django 2.2.6 on 2020-03-09 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waaam_app', '0003_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='areas_of_interest',
            field=models.TextField(blank=True, max_length=512),
        ),
        migrations.AddField(
            model_name='profile',
            name='background_check',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='distribution_list',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_aid_cpr',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='follow_up_email',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='harassment_training',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='medical_conditions',
            field=models.TextField(blank=True, max_length=512),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='profile',
            name='waiver_to_sign',
            field=models.TextField(blank=True, max_length=512),
        ),
        migrations.AddField(
            model_name='profile',
            name='was_interviewed',
            field=models.BooleanField(null=True),
        ),
    ]
