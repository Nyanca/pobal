# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-04 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20181203_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]