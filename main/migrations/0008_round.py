# Generated by Django 5.0.6 on 2024-05-14 09:54

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_myapply_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('round_number', models.CharField(max_length=35)),
                ('current', models.BooleanField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tournament')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
