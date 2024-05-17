# Generated by Django 5.0.6 on 2024-05-17 05:54

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('FullName', models.CharField(max_length=100)),
                ('PubgName', models.CharField(max_length=100)),
                ('PubgID', models.CharField(max_length=20)),
                ('point', models.IntegerField(blank=True, default=0, null=True)),
                ('played', models.IntegerField(blank=True, default=0, null=True)),
                ('win', models.IntegerField(blank=True, default=0, null=True)),
                ('lose', models.IntegerField(blank=True, default=0, null=True)),
                ('trophy', models.IntegerField(blank=True, default=0, null=True)),
                ('joined', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('round_number', models.CharField(max_length=35)),
                ('current', models.BooleanField(blank=True, null=True)),
                ('finished', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tournament_name', models.CharField(max_length=50)),
                ('tournament_name_uz', models.CharField(max_length=50, null=True)),
                ('tournament_name_en', models.CharField(max_length=50, null=True)),
                ('tournament_name_ru', models.CharField(max_length=50, null=True)),
                ('Prize', models.CharField(max_length=50)),
                ('tournament_image', models.ImageField(blank=True, null=True, upload_to='tournament/')),
                ('tournament_rules', models.TextField()),
                ('tournament_rules_uz', models.TextField(null=True)),
                ('tournament_rules_en', models.TextField(null=True)),
                ('tournament_rules_ru', models.TextField(null=True)),
                ('participants', models.TextField()),
                ('squad', models.CharField(choices=[('Solo', 'Solo'), ('Duo', 'Duo'), ('Squad', 'Squad')], max_length=30)),
                ('weapon', models.CharField(choices=[('M416', 'M416'), ('M24', 'M24'), ('All', 'All')], max_length=50)),
                ('started', models.BooleanField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('finished', models.BooleanField(blank=True, null=True)),
                ('available', models.BooleanField()),
                ('isfull', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TvVideo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('videoname', models.CharField(max_length=50)),
                ('videolink', models.CharField(max_length=200)),
                ('remove', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('player_1', models.CharField(max_length=50)),
                ('player_2', models.CharField(max_length=50)),
                ('overall_1', models.IntegerField(blank=True, default=0, null=True)),
                ('overall_2', models.IntegerField(blank=True, default=0, null=True)),
                ('matchvideo', models.CharField(blank=True, max_length=200, null=True)),
                ('tournament_winner', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('forround', models.ForeignKey(limit_choices_to={'finished': False}, on_delete=django.db.models.deletion.CASCADE, to='main.round')),
            ],
        ),
        migrations.AddField(
            model_name='round',
            name='tournament',
            field=models.ForeignKey(limit_choices_to={'finished': False}, on_delete=django.db.models.deletion.CASCADE, to='main.tournament'),
        ),
        migrations.CreateModel(
            name='MyApply',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('FullName', models.CharField(max_length=80)),
                ('PubgName', models.CharField(max_length=50)),
                ('PubgID', models.CharField(max_length=20)),
                ('tgusername', models.CharField(blank=True, max_length=50, null=True)),
                ('applydate', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(blank=True, null=True)),
                ('tournament_name', models.ForeignKey(limit_choices_to={'finished': False}, on_delete=django.db.models.deletion.CASCADE, to='main.tournament')),
            ],
        ),
    ]
