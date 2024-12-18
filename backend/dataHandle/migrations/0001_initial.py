# Generated by Django 5.1.4 on 2024-12-13 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userData',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=60)),
                ('userId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
