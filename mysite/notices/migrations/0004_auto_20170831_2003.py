# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0003_auto_20170830_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basenew',
            name='description',
            field=models.TextField(),
        ),
    ]