# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-31 13:06
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('name', models.CharField(max_length=141)),
                ('mana_cost', models.CharField(max_length=40)),
                ('cmc', models.DecimalField(decimal_places=2, max_digits=9)),
                ('type', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=400)),
                ('power', models.CharField(max_length=3)),
                ('toughness', models.CharField(max_length=3)),
                ('number', models.CharField(default='', max_length=4)),
                ('artist', models.CharField(default='', max_length=100)),
                ('id', models.SlugField(max_length=40, primary_key=True, serialize=False)),
                ('layout', models.IntegerField(choices=[(1, 'normal'), (2, 'flip'), (3, 'split'), (4, 'aftermath'), (5, 'token'), (6, 'double-faced'), (7, 'leveler'), (8, 'phenomenon'), (9, 'meld'), (10, 'vanguard'), (11, 'plane'), (12, 'scheme')], default=1)),
                ('rarity', models.IntegerField(choices=[(1, 'common'), (2, 'uncommon'), (3, 'rare'), (4, 'mythic rare'), (5, 'basic land'), (6, 'special')], default=1)),
                ('multiverse_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CardColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Card')),
            ],
        ),
        migrations.CreateModel(
            name='CardLegality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legality', models.IntegerField(choices=[(1, 'banned'), (2, 'restricted')], default=1)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('color', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ForeignCardName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('multiverse_id', models.PositiveIntegerField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Card')),
            ],
        ),
        migrations.CreateModel(
            name='ForeignLanguage',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MTGCryptoUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address1', models.CharField(max_length=300)),
                ('address2', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('country', models.CharField(default='', max_length=100)),
                ('timezone', models.CharField(max_length=20)),
                ('about', models.TextField(max_length=1000)),
                ('twitter', models.CharField(max_length=15)),
                ('on_vacation', models.BooleanField(default=False)),
                ('public', models.BooleanField(default=False)),
                ('since', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MTGSet',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Length has to be 3', regex='^\\w{3}$')])),
                ('name', models.CharField(max_length=40)),
                ('release_date', models.CharField(max_length=10)),
                ('type', models.IntegerField(choices=[(1, 'un'), (2, 'expansion'), (3, 'core'), (4, 'starter'), (5, 'box'), (6, 'reprint')], default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField()),
                ('quality', models.IntegerField(choices=[(1, 'mint'), (2, 'near mint'), (3, 'excellent'), (4, 'good'), (5, 'light played'), (6, 'played'), (7, 'poor')], default=1)),
                ('comment', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('foil', models.BooleanField(default=False)),
                ('signed', models.BooleanField(default=False)),
                ('altered', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=8, max_digits=20)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Card')),
                ('language', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ForeignCardName')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='foreigncardname',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ForeignLanguage'),
        ),
        migrations.AddField(
            model_name='cardlegality',
            name='format',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Format'),
        ),
        migrations.AddField(
            model_name='cardcolor',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Color'),
        ),
        migrations.AddField(
            model_name='card',
            name='mtgset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.MTGSet'),
        ),
    ]
