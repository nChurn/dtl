# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-14 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0046_auto_20180814_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertise',
            name='pretext_en',
            field=models.TextField(null=True, verbose_name='Текст цитаты'),
        ),
        migrations.AddField(
            model_name='expertise',
            name='pretext_ru',
            field=models.TextField(null=True, verbose_name='Текст цитаты'),
        ),
        migrations.AddField(
            model_name='expertise',
            name='title_en',
            field=models.CharField(max_length=240, null=True, verbose_name='Заголовок страницы'),
        ),
        migrations.AddField(
            model_name='expertise',
            name='title_ru',
            field=models.CharField(max_length=240, null=True, verbose_name='Заголовок страницы'),
        ),
    ]
