# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beer_googles', '0004_auto_20150406_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('bar', models.ForeignKey(to='beer_googles.Bar')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BeerComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Comment', models.TextField()),
                ('bar', models.ForeignKey(to='beer_googles.Bar')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='barrating',
            name='comment',
        ),
        migrations.AlterField(
            model_name='barrating',
            name='rating',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
