# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-06 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_auto_20171206_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertise',
            name='title',
            field=models.CharField(max_length=240, verbose_name='Заголовок страницы'),
        ),
    ]
