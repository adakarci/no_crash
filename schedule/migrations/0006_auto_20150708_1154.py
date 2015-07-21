# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.PositiveSmallIntegerField(default=0, choices=[(1, b'1.LESSON(08.00)'), (2, b'1.LESSON(08.00)'), (3, b'1.LESSON(08.00)'), (4, b'1.LESSON(08.00)')]),
        ),
    ]
