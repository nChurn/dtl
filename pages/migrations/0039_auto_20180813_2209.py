# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-13 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0038_auto_20180813_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='address_en',
            field=models.CharField(max_length=90, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='address_ru',
            field=models.CharField(max_length=90, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='title_en',
            field=models.CharField(max_length=40, null=True, verbose_name='Заголовок страницы'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='title_ru',
            field=models.CharField(max_length=40, null=True, verbose_name='Заголовок страницы'),
        ),
    ]
