# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 12:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('nummer', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Klas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Leraar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voornaam', models.CharField(max_length=100)),
                ('naam', models.CharField(max_length=100)),
                ('foto', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Richting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=100)),
                ('omschrijving', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='klas',
            name='leraar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schooltje.Leraar'),
        ),
        migrations.AddField(
            model_name='klas',
            name='richting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schooltje.Richting'),
        ),
    ]
