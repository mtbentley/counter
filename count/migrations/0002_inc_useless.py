# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inc',
            name='useless',
            field=models.CharField(max_length=16, default='RTFM'),
            preserve_default=True,
        ),
    ]
