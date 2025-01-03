# Generated by Django 5.1.4 on 2024-12-13 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataHandle', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='usersData',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=60)),
                ('userId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='userData',
        ),
    ]
