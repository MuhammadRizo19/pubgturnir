# Generated by Django 5.0.6 on 2024-05-14 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_myapply'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='isfull',
            field=models.BooleanField(default=False),
        ),
    ]
