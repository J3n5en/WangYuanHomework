# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_auto_20151024_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='comment',
            field=models.TextField(default='\u66ab\u7121\u8a55\u8ad6', verbose_name='\u8bc4\u8bba'),
        ),
        migrations.AlterField(
            model_name='design',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u63d0\u4ea4\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='design',
            name='desc',
            field=models.CharField(max_length=100, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='design',
            name='link',
            field=models.FileField(upload_to=b'./media/uploads', verbose_name='\u6587\u4ef6'),
        ),
        migrations.AlterField(
            model_name='design',
            name='owner',
            field=models.ForeignKey(related_name='DESIGNUSER', verbose_name='\u62e5\u6709\u8005', to='work.wy_user'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='comment',
            field=models.TextField(default='\u66ab\u7121\u8a55\u8ad6', verbose_name='\u8bc4\u8bba'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u63d0\u4ea4\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='desc',
            field=models.CharField(max_length=100, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='link',
            field=models.FileField(upload_to=b'./media/uploads', verbose_name='\u6587\u4ef6'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='owner',
            field=models.ForeignKey(related_name='CODEUSER', verbose_name='\u62e5\u6709\u8005', to='work.wy_user'),
        ),
        migrations.AlterField(
            model_name='newhomework',
            name='comment',
            field=models.TextField(default='\u66ab\u7121', verbose_name='\u8be6\u60c5'),
        ),
        migrations.AlterField(
            model_name='newhomework',
            name='desc',
            field=models.CharField(max_length=100, verbose_name='\u7b80\u4ecb'),
        ),
        migrations.AlterField(
            model_name='newhomework',
            name='link',
            field=models.FileField(upload_to=b'./media/uploads', verbose_name='\u6587\u4ef6'),
        ),
        migrations.AlterField(
            model_name='newhomework',
            name='owner',
            field=models.CharField(max_length=100, verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8'),
        ),
    ]
