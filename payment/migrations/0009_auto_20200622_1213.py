# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-06-22 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_auto_20200611_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='credit_amount',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
