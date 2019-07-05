# Generated by Django 2.2.3 on 2019-07-05 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineral',
            name='crystal_system',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='diaphaneity',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='optical_properties',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
