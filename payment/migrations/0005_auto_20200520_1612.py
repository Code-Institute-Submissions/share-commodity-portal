# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-05-20 16:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20200520_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commoditypricehistory',
            old_name='date',
            new_name='transaction_date',
        ),
        migrations.RenameField(
            model_name='sharepricehistory',
            old_name='date',
            new_name='transaction_date',
        ),
    ]