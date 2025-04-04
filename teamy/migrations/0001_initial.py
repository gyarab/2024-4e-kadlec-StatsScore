# Generated by Django 5.1.5 on 2025-01-26 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sporty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hrac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=100)),
                ('cislo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=100)),
                ('hraci', models.ManyToManyField(related_name='teams', to='teamy.hrac')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sporty.sport')),
            ],
        ),
        migrations.AddField(
            model_name='hrac',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='teamy.team'),
        ),
    ]
