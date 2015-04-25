# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer_googles', '0007_auto_20150420_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='slug',
            field=models.SlugField(default=b'', unique=True),
            preserve_default=True,
        ),
    ]
