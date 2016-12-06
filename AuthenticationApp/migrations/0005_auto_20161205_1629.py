# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UniversitiesApp', '0004_auto_20161108_1557'),
        ('AuthenticationApp', '0004_myuser_univ'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineer',
            name='university',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='UniversitiesApp.University'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_student',
            field=models.BooleanField(default=True),
        ),
    ]
