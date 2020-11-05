# Generated by Django 3.1.2 on 2020-10-23 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'regions',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location_system.region')),
            ],
            options={
                'db_table': 'provinces',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location_system.province')),
            ],
            options={
                'db_table': 'districts',
            },
        ),
    ]