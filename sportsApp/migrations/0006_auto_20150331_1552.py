# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0005_auto_20150325_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='champion',
        ),
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='defendingchampion',
        ),
        migrations.RemoveField(
            model_name='event',
            name='team',
        ),
        migrations.AddField(
            model_name='event',
            name='championMen',
            field=models.ForeignKey(related_name=b'championevent', blank=True, to='sportsApp.Athlete', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='defendingchampionMen',
            field=models.ForeignKey(related_name=b'defendingchampionevent', blank=True, to='sportsApp.Athlete', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='enddate',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='startdate',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='number',
            field=models.CharField(max_length=2),
        ),
    ]
