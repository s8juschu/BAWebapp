# Generated by Django 2.2.1 on 2019-05-23 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20190522_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Swimmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('size', models.CharField(max_length=30)),
                ('reps1', models.CharField(max_length=30)),
                ('reps2', models.CharField(max_length=30)),
                ('resttype', models.CharField(max_length=30)),
                ('resttime', models.IntegerField()),
                ('style', models.CharField(max_length=30)),
                ('comments', models.CharField(max_length=828)),
                ('tools', models.CharField(max_length=30)),
                ('distance', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.UserProfile')),
            ],
        ),
    ]
