# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-04 20:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='records',
            options={'verbose_name_plural': 'Records'},
        ),
    ]
