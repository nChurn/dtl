# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-22 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import proxima.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_actives'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionDirectionItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(default=1, max_length=10, verbose_name='Позиция')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Пункт',
                'verbose_name_plural': 'Пункты',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Заголовок страницы')),
                ('photo', models.ImageField(upload_to=proxima.utils.models.PathRename('expertise'), verbose_name='Фото под заголовком')),
                ('pretext', models.TextField(verbose_name='Текст цитаты')),
            ],
            options={
                'verbose_name': 'Экспертиза',
                'verbose_name_plural': 'Экспертиза',
            },
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(default=1, max_length=10, verbose_name='Позиция')),
                ('title', models.CharField(max_length=200, verbose_name='Название отрасли')),
            ],
            options={
                'verbose_name': 'Отрасль',
                'verbose_name_plural': 'Отрасли',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240, verbose_name='Название')),
                ('photo', models.ImageField(upload_to=proxima.utils.models.PathRename('news/previews'), verbose_name='Фото на ховере превью')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('pretext', models.TextField(verbose_name='Текст цитаты')),
                ('photo1', models.ImageField(upload_to=proxima.utils.models.PathRename('news/photos'), verbose_name='Фото')),
                ('subtitle1', models.CharField(max_length=300, verbose_name='Подзаголовок 1')),
                ('text1', models.TextField(verbose_name='Текст 1')),
                ('subtitle2', models.CharField(max_length=300, verbose_name='Подзаголовок 2')),
                ('text2', models.TextField(verbose_name='Текст 2')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='NewsPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Заголовок страницы')),
                ('photo', models.ImageField(upload_to=proxima.utils.models.PathRename('projects'), verbose_name='Фото под заголовком')),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новость',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=100, verbose_name='Клиент')),
                ('title', models.CharField(max_length=240, verbose_name='Название')),
                ('logo', models.ImageField(upload_to=proxima.utils.models.PathRename('projects/logos'), verbose_name='Лого на превью')),
                ('photo', models.ImageField(upload_to=proxima.utils.models.PathRename('projects/previews'), verbose_name='Фото на ховере превью')),
                ('is_active', models.BooleanField(default=False, verbose_name='Является ли активом?')),
                ('position', models.CharField(default=1, max_length=10, verbose_name='Позиция')),
                ('logo_head', models.ImageField(upload_to=proxima.utils.models.PathRename('projects/logos'), verbose_name='Лого в шапке')),
                ('photo_head', models.ImageField(upload_to=proxima.utils.models.PathRename('projects/photos'), verbose_name='Фото в шапке')),
                ('inv', models.CharField(max_length=15, verbose_name='Инвестиции PCG')),
                ('per', models.CharField(max_length=30, verbose_name='Период реализации')),
                ('geo', models.CharField(max_length=15, verbose_name='География проекта')),
                ('pretext', models.TextField(verbose_name='Текст цитаты')),
                ('text', models.TextField(verbose_name='Текст основной')),
                ('subtitle', models.CharField(max_length=300, verbose_name='Подзаголовок')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='ProjectItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(default=1, max_length=10, verbose_name='Позиция')),
                ('text', models.TextField(verbose_name='Текст основной')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Project', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Пункт',
                'verbose_name_plural': 'Пункты',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='ProjectPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Заголовок страницы')),
                ('photo', models.ImageField(upload_to=proxima.utils.models.PathRename('projects'), verbose_name='Фото под заголовком')),
            ],
            options={
                'verbose_name': 'Проекты',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.AddField(
            model_name='actiondirection',
            name='photo',
            field=models.ImageField(default=1, upload_to=proxima.utils.models.PathRename('directions'), verbose_name='Фото под заголовком'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actiondirection',
            name='pretext',
            field=models.TextField(default=1, verbose_name='Текст цитаты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actiondirection',
            name='subtitle',
            field=models.CharField(default=1, max_length=300, verbose_name='Подзаголовок'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actiondirection',
            name='text',
            field=models.TextField(default=1, verbose_name='Основной текст'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='actions',
            field=models.ManyToManyField(blank=True, to='pages.ActionDirection'),
        ),
        migrations.AddField(
            model_name='project',
            name='industries',
            field=models.ManyToManyField(blank=True, to='pages.Industry'),
        ),
        migrations.AddField(
            model_name='project',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.ProjectPage', verbose_name='Страница'),
        ),
        migrations.AddField(
            model_name='news',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.NewsPage', verbose_name='Страница'),
        ),
        migrations.AddField(
            model_name='news',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Project', verbose_name='Выбор проекта'),
        ),
        migrations.AddField(
            model_name='expertise',
            name='actions',
            field=models.ManyToManyField(blank=True, to='pages.ActionDirection'),
        ),
        migrations.AddField(
            model_name='actiondirectionitems',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.ActionDirection'),
        ),
    ]
