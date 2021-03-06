# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-14 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0045_auto_20180814_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='actives',
            name='block1_subtitle_en',
            field=models.CharField(max_length=300, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block1_subtitle_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block1_text_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block1_text_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block1_title_en',
            field=models.CharField(max_length=300, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block1_title_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block2_item1_en',
            field=models.TextField(null=True, verbose_name='Текст пункта 1'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block2_item1_ru',
            field=models.TextField(null=True, verbose_name='Текст пункта 1'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block2_item2_en',
            field=models.TextField(null=True, verbose_name='Текст пункта 2'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block2_item2_ru',
            field=models.TextField(null=True, verbose_name='Текст пункта 2'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block2_item3_en',
            field=models.TextField(null=True, verbose_name='Текст пункта 3'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block2_item3_ru',
            field=models.TextField(null=True, verbose_name='Текст пункта 3'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block2_subtitle_en',
            field=models.CharField(max_length=300, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block2_subtitle_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block3_subtitle_en',
            field=models.CharField(max_length=300, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block3_subtitle_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block3_text_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block3_text_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block4_subtitle_en',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block4_subtitle_ru',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block4_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='actives',
            name='block4_text_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='actives',
            name='pretext_en',
            field=models.TextField(null=True, verbose_name='Текст цитаты'),
        ),
        migrations.AddField(
            model_name='actives',
            name='pretext_ru',
            field=models.TextField(null=True, verbose_name='Текст цитаты'),
        ),
        migrations.AddField(
            model_name='actives',
            name='title_en',
            field=models.CharField(max_length=40, null=True, verbose_name='Заголовок страницы'),
        ),
        migrations.AddField(
            model_name='actives',
            name='title_ru',
            field=models.CharField(max_length=40, null=True, verbose_name='Заголовок страницы'),
        ),
    ]
