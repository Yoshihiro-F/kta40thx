# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-22 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planyear',
            name='up_date',
            field=models.DateTimeField(auto_now=True, verbose_name='編集日時'),
        ),
    ]