# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0005_auto_20150325_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date',
            new_name='enddate',
        ),
        migrations.AddField(
            model_name='event',
            name='startdate',
            field=models.DateField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='champion',
            field=models.ForeignKey(related_name=b'championevent', blank=True, to='sportsApp.Athlete', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='defendingchampion',
            field=models.ForeignKey(related_name=b'defendingchampionevent', blank=True, to='sportsApp.Athlete', null=True),
        ),
    ]
