# Generated by Django 5.1.4 on 2025-02-14 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_genre_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'managed': False},
        ),
    ]
