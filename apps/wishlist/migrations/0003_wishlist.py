# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-13 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_user_date_hired'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('date_added', models.DateField(default='2018-04-13')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_items', to='wishlist.User')),
                ('wished_by', models.ManyToManyField(related_name='wished_by', to='wishlist.User')),
            ],
        ),
    ]