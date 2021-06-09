# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-22 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20171122_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Заголовок страницы')),
                ('address', models.CharField(max_length=90, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=90, verbose_name='Телефон')),
                ('email', models.CharField(max_length=90, verbose_name='E-mail')),
                ('lat', models.CharField(max_length=40, verbose_name='Координата широты')),
                ('lng', models.CharField(max_length=40, verbose_name='Координата долготы')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]