# Generated by Django 5.0.2 on 2024-04-06 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_records'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]
