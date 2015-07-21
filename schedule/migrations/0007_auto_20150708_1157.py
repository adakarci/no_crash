# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_auto_20150708_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.PositiveSmallIntegerField(default=0, choices=[(1, b'1.LESSON(08.00)'), (2, b'1.LESSON(08.00)'), (3, b'1.LESSON(08.00)'), (4, b'1.LESSON(08.00)')]),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
    ]
