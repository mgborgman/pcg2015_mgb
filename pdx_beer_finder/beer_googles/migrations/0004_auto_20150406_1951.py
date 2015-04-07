# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer_googles', '0003_auto_20150406_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrating',
            name='comment',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barrating',
            name='rating',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
