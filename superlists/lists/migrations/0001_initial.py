# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Tytul')),
                ('description', models.TextField(verbose_name='Opis')),
                ('created', models.DateTimeField(verbose_name='Data dodania')),
                ('finished', models.DateTimeField(verbose_name='Termin zakonczenia')),
                ('assign', models.CharField(max_length=100)),
            ],
        ),
    ]