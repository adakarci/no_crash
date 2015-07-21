# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=2000)),
                ('event_type', models.PositiveSmallIntegerField(default=0, choices=[(0, b'Examination '), (1, b'Lab Lesson'), (2, b'Ceremony'), (3, b'Festival')])),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('decline', models.CharField(max_length=2000, null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
