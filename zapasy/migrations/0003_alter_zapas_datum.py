# Generated by Django 5.1.6 on 2025-02-24 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapasy', '0002_liga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapas',
            name='datum',
            field=models.DateTimeField(),
        ),
    ]
