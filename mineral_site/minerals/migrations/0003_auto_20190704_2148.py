# Generated by Django 2.2.3 on 2019-07-05 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0002_auto_20190704_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineral',
            name='refractive_index',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='specific_gravity',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
