# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-13 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_hired',
            field=models.DateField(default='2018-04-13'),
        ),
    ]
