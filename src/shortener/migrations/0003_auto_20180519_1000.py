# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-05-19 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_kirrurl_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
