# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-29 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('university', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=500)),
            ],
        ),
    ]