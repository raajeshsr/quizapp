# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-10 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20180210_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]