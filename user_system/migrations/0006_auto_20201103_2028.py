# Generated by Django 3.1.2 on 2020-11-04 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_system', '0005_auto_20201023_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='organization',
            field=models.CharField(default='', max_length=90),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='ruc',
            field=models.CharField(default='', max_length=11),
            preserve_default=False,
        ),
    ]