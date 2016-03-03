# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_auto_20151022_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wy_user',
            name='phonenumber',
            field=models.CharField(max_length=20),
        ),
    ]
