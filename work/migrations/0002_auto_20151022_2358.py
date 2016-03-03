# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='design',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterModelOptions(
            name='homework',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterModelOptions(
            name='newhomework',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterField(
            model_name='wy_user',
            name='phonenumber',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
