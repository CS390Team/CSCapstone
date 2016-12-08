# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UniversitiesApp', '0001_initial'),
        ('GroupsApp', '0001_initial'),
        ('AuthenticationApp', '0002_auto_20161208_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(default=None, to='UniversitiesApp.Course'),
        ),
        migrations.AddField(
            model_name='student',
            name='groups',
            field=models.ManyToManyField(default=None, to='GroupsApp.Group'),
        ),
    ]
