# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-13 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0001_initial'),
        ('naturalUser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ONGLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('natural_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naturalUser.NaturalUser')),
                ('ong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ong.ONG')),
            ],
        ),
    ]
