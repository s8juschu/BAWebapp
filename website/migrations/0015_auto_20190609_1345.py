# Generated by Django 2.2.1 on 2019-06-09 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20190609_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planrow',
            old_name='reps1',
            new_name='rep1',
        ),
        migrations.RenameField(
            model_name='planrow',
            old_name='reps2',
            new_name='rep2',
        ),
    ]
