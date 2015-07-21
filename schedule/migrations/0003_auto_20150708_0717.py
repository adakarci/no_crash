# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.TextField(max_length=2000),
        ),
    ]
