# Generated by Django 3.1.3 on 2020-11-20 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='operation_date',
            field=models.DateField(null=True, unique=True),
        ),
    ]
