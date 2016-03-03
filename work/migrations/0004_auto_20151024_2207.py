# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0003_auto_20151024_2021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='design',
            options={'ordering': ['-pk'], 'verbose_name': '\u8bbe\u8ba1\u4f5c\u4e1a', 'verbose_name_plural': '\u8bbe\u8ba1\u4f5c\u4e1a'},
        ),
        migrations.AlterModelOptions(
            name='homework',
            options={'ordering': ['-pk'], 'verbose_name': '\u4ee3\u7801\u4f5c\u4e1a', 'verbose_name_plural': '\u4ee3\u7801\u4f5c\u4e1a'},
        ),
        migrations.AlterModelOptions(
            name='newhomework',
            options={'ordering': ['-pk'], 'verbose_name': '\u5e03\u7f6e\u65b0\u4f5c\u4e1a', 'verbose_name_plural': '\u5e03\u7f6e\u65b0\u4f5c\u4e1a'},
        ),
        migrations.AlterModelOptions(
            name='wy_user',
            options={'ordering': ['-user_name'], 'verbose_name': '\u7528\u6237', 'verbose_name_plural': '\u7528\u6237'},
        ),
        migrations.AlterField(
            model_name='wy_user',
            name='phonenumber',
            field=models.CharField(max_length=20, verbose_name='\u7535\u8bdd\u53f7\u7801'),
        ),
        migrations.AlterField(
            model_name='wy_user',
            name='user_name',
            field=models.CharField(unique=True, max_length=10, verbose_name='\u7528\u6237\u540d'),
        ),
    ]
