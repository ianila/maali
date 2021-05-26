# Generated by Django 3.2.3 on 2021-05-26 17:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_maaliuser_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maaliuser',
            name='last_login',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
