# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-13 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0037_project_title_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpage',
            name='first_subtext_en',
            field=models.CharField(max_length=300, null=True, verbose_name='Подзаголовок слайда'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='first_subtext_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Подзаголовок слайда'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='fourth_text_en',
            field=models.TextField(null=True, verbose_name='Заголовок слайда'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='fourth_text_ru',
            field=models.TextField(null=True, verbose_name='Заголовок слайда'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='second_subtext_en',
            field=models.CharField(max_length=300, null=True, verbose_name='Текст справа от кнопки'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='second_subtext_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Текст справа от кнопки'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='second_text_en',
            field=models.TextField(null=True, verbose_name='Заголовок слайда'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='second_text_ru',
            field=models.TextField(null=True, verbose_name='Заголовок слайда'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='third_text_en',
            field=models.TextField(null=True, verbose_name='Заголовок слайда'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='third_text_ru',
            field=models.TextField(null=True, verbose_name='Заголовок слайда'),
        ),
    ]
