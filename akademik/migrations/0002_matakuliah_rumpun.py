# Generated by Django 4.2.11 on 2024-07-27 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matakuliah',
            name='rumpun',
            field=models.CharField(blank=True, choices=[('Institusi', 'Institusi'), ('Prodi', 'Prodi')], max_length=20, null=True),
        ),
    ]
