# Generated by Django 4.2.5 on 2023-10-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_alter_datasiswa_tahun'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasiswa',
            name='tahun',
            field=models.IntegerField(default=2023, verbose_name='Tahun'),
        ),
    ]
