# Generated by Django 5.1.6 on 2025-02-24 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamy', '0002_remove_hrac_team_alter_team_hraci'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrac',
            name='cislo',
            field=models.IntegerField(unique=True),
        ),
    ]
