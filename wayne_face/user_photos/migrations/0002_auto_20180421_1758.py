# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-21 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userphoto',
            name='photo',
            field=models.CharField(max_length=256),
        ),
    ]