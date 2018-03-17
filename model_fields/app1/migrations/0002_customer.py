# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-17 04:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Company')),
            ],
        ),
    ]
