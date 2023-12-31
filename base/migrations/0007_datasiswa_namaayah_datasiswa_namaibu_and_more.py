# Generated by Django 4.2.5 on 2023-10-05 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_datasiswa_tahun'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasiswa',
            name='namaAyah',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='datasiswa',
            name='namaIbu',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='datasiswa',
            name='nikAyah',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datasiswa',
            name='nikIbu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datasiswa',
            name='noKip',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datasiswa',
            name='noPkh',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datasiswa',
            name='pekerjaanAyah',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='datasiswa',
            name='pekerjaanIbu',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
