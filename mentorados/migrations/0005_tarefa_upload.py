# Generated by Django 5.1.7 on 2025-04-05 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorados', '0004_reuniao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarefa', models.CharField(max_length=255)),
                ('realizada', models.BooleanField(default=False)),
                ('mentorado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mentorados.mentorados')),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='video')),
                ('mentorado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mentorados.mentorados')),
            ],
        ),
    ]
