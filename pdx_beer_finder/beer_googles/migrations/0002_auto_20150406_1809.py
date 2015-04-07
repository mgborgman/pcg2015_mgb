# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer_googles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bars',
            new_name='Bar',
        ),
        migrations.AlterModelOptions(
            name='bar',
            options={'verbose_name': 'Bar', 'verbose_name_plural': 'Bars'},
        ),
        migrations.AlterModelOptions(
            name='beer',
            options={'verbose_name': 'Beer', 'verbose_name_plural': 'Beers'},
        ),
    ]
