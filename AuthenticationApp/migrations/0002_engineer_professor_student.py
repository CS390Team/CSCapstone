# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-06 16:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UniversitiesApp', '0001_initial'),
        ('CompaniesApp', '0001_initial'),
        ('AuthenticationApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='CompaniesApp.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('university', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='UniversitiesApp.University')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('university', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='UniversitiesApp.University')),
            ],
        ),
    ]