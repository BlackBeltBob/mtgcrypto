# Generated by Django 2.0.7 on 2018-07-27 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20180727_0737'),
    ]

    operations = [
        migrations.CreateModel(
            name='MTGCryptoUser',
            fields=[
                ('username', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=200)),
                ('address1', models.CharField(max_length=300)),
                ('address2', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('timezone', models.CharField(max_length=20)),
                ('about', models.TextField(max_length=1000)),
                ('twitter', models.CharField(max_length=15)),
                ('on_vacation', models.BooleanField(default=False)),
                ('public', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=100)),
                ('since', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.SmallIntegerField()),
                ('quality', models.IntegerField(choices=[(1, 'mint'), (2, 'near mint'), (3, 'excellent'), (4, 'good'), (5, 'light played'), (6, 'played'), (7, 'poor')], default=1)),
                ('comment', models.CharField(max_length=50)),
                ('foil', models.BooleanField(default=False)),
                ('signed', models.BooleanField(default=False)),
                ('altered', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=8, max_digits=20)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Card')),
            ],
        ),
        migrations.AlterField(
            model_name='foreigncardname',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Card'),
        ),
        migrations.AddField(
            model_name='offer',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ForeignCardName'),
        ),
        migrations.AddField(
            model_name='offer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.MTGCryptoUser'),
        ),
    ]
