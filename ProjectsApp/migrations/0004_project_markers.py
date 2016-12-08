# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 11:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ProjectsApp', '0003_auto_20161208_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='markers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
