# Generated by Django 3.1.5 on 2022-08-08 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geolocalizaciones', '0002_auto_20220807_0052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'ordering': ['id'], 'verbose_name': 'Ciudad', 'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='estado',
            options={'ordering': ['id'], 'verbose_name': 'Estado', 'verbose_name_plural': 'Estados'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'ordering': ['id'], 'verbose_name': 'País', 'verbose_name_plural': 'Paises'},
        ),
    ]