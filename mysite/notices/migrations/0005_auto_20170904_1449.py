# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0004_auto_20170831_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basenew',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
