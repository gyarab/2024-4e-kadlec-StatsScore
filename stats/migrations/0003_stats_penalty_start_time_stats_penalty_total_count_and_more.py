# Generated by Django 5.1.6 on 2025-02-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_stats_disqualified'),
        ('teamy', '0004_alter_hrac_cislo'),
        ('zapasy', '0004_zapas_elapsed_time_zapas_pause_time_zapas_start_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='penalty_start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stats',
            name='penalty_total_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stats',
            name='goly',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stats',
            name='trestne_minuty',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stats',
            name='zlute_karty',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='stats',
            unique_together={('zapas', 'hrac')},
        ),
    ]
