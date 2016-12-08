# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroupsApp', '0002_group_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='experience',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='languages',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='speciality',
            field=models.CharField(max_length=200, null=True),
        ),
    ]