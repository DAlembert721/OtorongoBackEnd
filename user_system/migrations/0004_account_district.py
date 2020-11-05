# Generated by Django 3.1.2 on 2020-10-23 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location_system', '0001_initial'),
        ('user_system', '0003_account_maintenance'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='location_system.district'),
        ),
    ]