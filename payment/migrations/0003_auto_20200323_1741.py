# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-03-23 17:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_commoditypricehistory_commoditypurchase_sharepricehistory_sharepurchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commoditypurchase',
            name='price',
        ),
        migrations.RemoveField(
            model_name='sharepurchase',
            name='price',
        ),
    ]
