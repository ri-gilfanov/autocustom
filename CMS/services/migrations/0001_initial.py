# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 04:19
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='наименование товара')),
                ('slug', models.SlugField(allow_unicode=True, max_length=64, unique=True, verbose_name='человекопонятный url-адрес')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='описание товара')),
            ],
            options={
                'verbose_name_plural': 'услуги',
                'verbose_name': 'услуга',
            },
        ),
    ]