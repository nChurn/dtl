# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-05 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_auto_20171205_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='block4_item2',
            field=models.TextField(blank=True, verbose_name='Текст пункта 2'),
        ),
        migrations.AlterField(
            model_name='about',
            name='block4_item4',
            field=models.TextField(blank=True, verbose_name='Текст пункта 4'),
        ),
    ]