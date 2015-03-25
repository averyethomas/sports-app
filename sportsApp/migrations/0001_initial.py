# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('rank', models.IntegerField(max_length=2)),
                ('points', models.IntegerField(max_length=10)),
                ('earnings', models.IntegerField(max_length=15)),
                ('jerseyNumber', models.IntegerField(max_length=2)),
                ('CTHeatWins', models.IntegerField(max_length=10)),
                ('avgHeatScore', models.IntegerField(max_length=10)),
                ('hometown', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('height', models.CharField(max_length=6)),
                ('weight', models.IntegerField(max_length=3)),
                ('dob', models.CharField(max_length=10)),
                ('winnings', models.CharField(max_length=20)),
                ('instagram', models.CharField(unique=True, max_length=20)),
                ('twitter', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'ordering': ('gender', 'rank'),
                'verbose_name_plural': 'Athletes',
            },
            bases=(models.Model,),
        ),
    ]
