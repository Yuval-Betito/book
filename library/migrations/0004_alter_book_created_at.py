# Generated by Django 5.1.4 on 2025-01-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_genre_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
