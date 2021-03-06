# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20170607_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='1', max_length=64, unique=True, verbose_name='человекопонятный url-адрес'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='наименование товара'),
        ),
    ]
