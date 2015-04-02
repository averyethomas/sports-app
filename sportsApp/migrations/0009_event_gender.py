# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0008_auto_20150401_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='gender',
            field=models.CharField(default=b'm', max_length=1),
            preserve_default=True,
        ),
    ]
