# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-06 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_auto_20171205_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=350, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок страницы'),
        ),
    ]
