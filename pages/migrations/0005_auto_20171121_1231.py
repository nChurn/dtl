# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-21 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_docs_documentation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='people',
            field=models.ManyToManyField(blank=True, to='pages.Person'),
        ),
    ]
