# Generated by Django 2.2.3 on 2019-07-05 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image_filename', models.CharField(max_length=255)),
                ('image_caption', models.TextField(default='')),
                ('category', models.CharField(default='', max_length=255)),
                ('formula', models.TextField(default='')),
                ('strunz_classification', models.CharField(max_length=255)),
                ('color', models.TextField(default='')),
                ('crystal_system', models.CharField(max_length=255)),
                ('unit_cell', models.CharField(max_length=255)),
                ('crystal_symmetry', models.CharField(max_length=255)),
                ('cleavage', models.CharField(max_length=255)),
                ('mohs_scale_hardness', models.CharField(max_length=255)),
                ('luster', models.CharField(max_length=255)),
                ('streak', models.CharField(max_length=255)),
                ('diaphaneity', models.CharField(max_length=255)),
                ('optical_properties', models.CharField(max_length=255)),
                ('refractive_index', models.CharField(max_length=255)),
                ('crystal_habit', models.TextField(default='')),
                ('specific_gravity', models.CharField(max_length=255)),
                ('group', models.CharField(default='', max_length=255)),
            ],
        ),
    ]