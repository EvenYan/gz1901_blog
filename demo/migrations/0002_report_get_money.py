# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-06-16 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='get_money',
            field=models.PositiveIntegerField(default=300),
        ),
    ]
