# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-31 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='power',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='toughness',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
    ]
