# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0007_auto_20150331_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='number',
            field=models.IntegerField(),
        ),
    ]
