# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-31 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_card_loyalty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='number',
            field=models.CharField(max_length=4),
        ),
    ]
