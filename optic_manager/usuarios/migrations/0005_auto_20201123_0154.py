# Generated by Django 3.1.2 on 2020-11-23 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20201122_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='turno',
            name='asistencia',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
