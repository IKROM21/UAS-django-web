# Generated by Django 4.2.5 on 2023-10-09 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_alter_datasiswa_tahun'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasiswa',
            name='tahun',
            field=models.DateField(default=datetime.datetime(2023, 10, 9, 13, 45, 41, 329927, tzinfo=datetime.timezone.utc)),
        ),
    ]
