# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-21 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pobalStudio', '0005_auto_20181119_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, default='img/pobal_sphere.png', null=True, upload_to='img'),
        ),
    ]
