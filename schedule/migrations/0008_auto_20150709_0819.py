# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_auto_20150708_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='name',
        ),
        migrations.AddField(
            model_name='event',
            name='content',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.PositiveSmallIntegerField(default=0, choices=[(1, b'1.LESSON(08.00)'), (2, b'1.LESSON(09.00)'), (3, b'1.LESSON(010.00)'), (4, b'1.LESSON(011.00)')]),
        ),
    ]
