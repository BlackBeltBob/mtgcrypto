# Generated by Django 2.0.7 on 2018-07-27 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_card_layout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Format',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
