# Generated by Django 3.1.3 on 2020-11-23 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_system', '0004_auto_20201121_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='payed',
            field=models.FloatField(default=0),
        ),
    ]
