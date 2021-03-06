# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-23 08:50
from __future__ import unicode_literals

from django.db import migrations, models
import proxima.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20171122_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='category',
            field=models.CharField(choices=[('sp', 'Специалистам'), ('st', 'Студентам')], default='sp', max_length=2, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='file',
            field=models.FileField(blank=True, upload_to=proxima.utils.models.PathRename('resume'), verbose_name='Файл'),
        ),
    ]
