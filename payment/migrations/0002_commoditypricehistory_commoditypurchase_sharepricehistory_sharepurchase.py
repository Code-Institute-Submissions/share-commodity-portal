# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-03-23 16:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_commodity_unit'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommodityPriceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.Commodity')),
            ],
        ),
        migrations.CreateModel(
            name='CommodityPurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.Commodity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SharePriceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('share', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.Share')),
            ],
        ),
        migrations.CreateModel(
            name='SharePurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('share', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.Share')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
