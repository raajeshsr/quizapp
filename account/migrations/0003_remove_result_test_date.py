# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-22 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_result_test_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='test_date',
        ),
    ]
