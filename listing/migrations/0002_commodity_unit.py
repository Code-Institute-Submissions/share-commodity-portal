# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-03-11 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='unit',
            field=models.CharField(default='', max_length=254),
        ),
    ]