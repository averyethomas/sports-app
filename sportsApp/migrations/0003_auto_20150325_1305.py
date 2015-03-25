# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0002_auto_20150325_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='avgHeatScore',
            field=models.CharField(max_length=10),
        ),
    ]
