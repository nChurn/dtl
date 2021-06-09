# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-21 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import proxima.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_career_careeradvantages_careerdemands_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, verbose_name='Название')),
                ('file', models.FileField(upload_to=proxima.utils.models.PathRename('docs'), verbose_name='Файл')),
                ('position', models.CharField(default=1, max_length=10, verbose_name='Позиция')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Career', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Заголовок страницы')),
                ('photo', models.ImageField(upload_to=proxima.utils.models.PathRename('career'), verbose_name='Фото под заголовком')),
            ],
            options={
                'verbose_name': 'Документация',
                'verbose_name_plural': 'Документация',
            },
        ),
    ]
