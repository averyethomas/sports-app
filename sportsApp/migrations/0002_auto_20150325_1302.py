# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='instagram',
            field=models.CharField(unique=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='twitter',
            field=models.CharField(unique=True, max_length=20, blank=True),
        ),
    ]
