# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 19:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_mymodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
