# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-06 01:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0006_auto_20161206_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineer',
            name='university',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='UniversitiesApp.University'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='university',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='UniversitiesApp.University'),
        ),
        migrations.AlterField(
            model_name='student',
            name='university',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='UniversitiesApp.University'),
        ),
    ]
