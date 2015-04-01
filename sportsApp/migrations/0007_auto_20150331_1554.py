# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0006_auto_20150331_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
