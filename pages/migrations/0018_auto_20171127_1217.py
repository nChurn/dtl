# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-27 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_remove_projectpage_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage',
            name='fourth_text',
            field=models.TextField(max_length=165, verbose_name='Заголовок слайда'),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='second_text',
            field=models.TextField(max_length=240, verbose_name='Заголовок слайда'),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='third_text',
            field=models.TextField(max_length=240, verbose_name='Заголовок слайда'),
        ),
    ]