# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0004_auto_20150325_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='avatar',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'avatars', blank=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='photo1',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'photos', blank=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='photo2',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'photos', blank=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='photo3',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'photos', blank=True),
        ),
    ]
