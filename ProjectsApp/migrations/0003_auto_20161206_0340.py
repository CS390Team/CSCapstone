# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-06 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectsApp', '0002_auto_20161206_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='pro_language',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='speciality',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='years_of_exp',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
