# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0003_auto_20150325_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('date', models.DateField()),
                ('number', models.CharField(unique=True, max_length=2)),
                ('location', models.CharField(unique=True, max_length=50)),
                ('champion', models.ForeignKey(related_name=b'championevent', to='sportsApp.Athlete', null=True)),
                ('defendingchampion', models.ForeignKey(related_name=b'defendingchampionevent', to='sportsApp.Athlete', null=True)),
            ],
            options={
                'ordering': ('number',),
                'verbose_name_plural': 'Events',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Teams',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='team',
            field=models.ForeignKey(to='sportsApp.Team'),
            preserve_default=True,
        ),
        migrations.AlterModelOptions(
            name='athlete',
            options={'ordering': ('rank',), 'verbose_name_plural': 'Athletes'},
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='gender',
        ),
        migrations.AddField(
            model_name='athlete',
            name='avatar',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'avatars'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='athlete',
            name='photo1',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'photos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='athlete',
            name='photo2',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'photos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='athlete',
            name='photo3',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'photos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='athlete',
            name='team',
            field=models.ForeignKey(to='sportsApp.Team', null=True),
            preserve_default=True,
        ),
    ]
