# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-22 22:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('footer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Related',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_name', models.CharField(max_length=30, verbose_name='関連リンク名')),
                ('link_url', models.URLField(verbose_name='URL')),
            ],
        ),
        migrations.RemoveField(
            model_name='footer',
            name='link_name',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='link_url',
        ),
        migrations.AddField(
            model_name='related',
            name='footer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footer.Footer'),
        ),
    ]
