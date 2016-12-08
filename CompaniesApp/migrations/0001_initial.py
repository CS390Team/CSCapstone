# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 06:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('photo', models.ImageField(default=0, upload_to=b'static/companyimages')),
                ('description', models.CharField(max_length=300)),
                ('website', models.CharField(default=b'/', max_length=300)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
