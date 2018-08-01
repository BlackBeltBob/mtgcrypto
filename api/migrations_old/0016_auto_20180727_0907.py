# Generated by Django 2.0.7 on 2018-07-27 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0015_auto_20180727_0830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mtgcryptouser',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='mtgcryptouser',
            name='password',
        ),
        migrations.RemoveField(
            model_name='mtgcryptouser',
            name='username',
        ),
        migrations.AddField(
            model_name='mtgcryptouser',
            name='country',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='mtgcryptouser',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
