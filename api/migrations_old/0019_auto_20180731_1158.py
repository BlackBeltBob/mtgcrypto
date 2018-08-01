# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-31 11:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_card_rarity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='language',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ForeignCardName'),
        ),
    ]
