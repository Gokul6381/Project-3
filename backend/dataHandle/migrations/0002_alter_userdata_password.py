# Generated by Django 5.1.4 on 2024-12-13 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataHandle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]