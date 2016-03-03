# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='design',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc', models.CharField(max_length=100)),
                ('link', models.FileField(upload_to=b'./media/uploads')),
                ('comment', models.TextField(default='\u66ab\u7121\u8a55\u8ad6')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='homework',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc', models.CharField(max_length=100)),
                ('link', models.FileField(upload_to=b'./media/uploads')),
                ('comment', models.TextField(default='\u66ab\u7121\u8a55\u8ad6')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='newhomework',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('link', models.FileField(upload_to=b'./media/uploads')),
                ('comment', models.TextField(default='\u66ab\u7121')),
            ],
        ),
        migrations.CreateModel(
            name='wy_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(unique=True, max_length=10)),
                ('phonenumber', models.IntegerField(unique=True)),
            ],
            options={
                'ordering': ['-user_name'],
            },
        ),
        migrations.AddField(
            model_name='homework',
            name='owner',
            field=models.ForeignKey(related_name='CODEUSER', to='work.wy_user'),
        ),
        migrations.AddField(
            model_name='design',
            name='owner',
            field=models.ForeignKey(related_name='DESIGNUSER', to='work.wy_user'),
        ),
    ]
