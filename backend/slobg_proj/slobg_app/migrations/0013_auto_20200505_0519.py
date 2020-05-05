# Generated by Django 2.2.6 on 2020-05-05 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slobg_app', '0012_merge_20200504_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteerrecord',
            name='desc',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='volunteerrecord',
            name='activity',
            field=models.CharField(choices=[('Maintenance', 'Maintenance'), ('Administration', 'Administration'), ('Outreach', 'Outreach'), ('Education', 'Education'), ('Propagation', 'Propagation'), ('Other', 'Other')], max_length=256),
        ),
    ]
