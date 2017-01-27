# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('codigo', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feedback', models.CharField(max_length=200)),
                ('fk_actividad', models.ForeignKey(to='workflow.Actividad')),
            ],
        ),
        migrations.CreateModel(
            name='Shopper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('nro_telefono', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='feedbacks',
            name='fk_shopper',
            field=models.ForeignKey(to='workflow.Shopper'),
        ),
    ]
