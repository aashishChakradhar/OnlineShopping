# Generated by Django 5.0.3 on 2024-03-17 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
