# Generated by Django 2.2.1 on 2019-06-05 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20190605_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanRow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps1', models.CharField(max_length=30)),
                ('reps2', models.CharField(max_length=30)),
                ('distance', models.IntegerField()),
                ('resttype', models.CharField(max_length=30)),
                ('resttime', models.IntegerField()),
                ('style', models.CharField(max_length=30)),
                ('comments', models.CharField(max_length=828)),
                ('tools', models.CharField(max_length=30)),
                ('effort', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('size', models.CharField(max_length=30)),
                ('planrows', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.PlanRow')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.UserProfile')),
            ],
        ),
    ]