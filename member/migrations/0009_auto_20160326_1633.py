# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-26 07:33
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_memberlist_orderid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberlist',
            name='image',
            field=models.ImageField(blank=True, help_text='画像は任意で', storage=django.core.files.storage.FileSystemStorage(location='static/media/'), upload_to='memberphoto/', verbose_name='画像'),
        ),
    ]
