# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-11 17:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20180111_1457'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Userdata',
        ),
    ]
