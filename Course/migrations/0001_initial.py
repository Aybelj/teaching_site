# Generated by Django 3.1.1 on 2020-09-26 05:32

import Course.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('position', models.PositiveSmallIntegerField()),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='Images')),
                ('video', models.FileField(blank=True, upload_to='images/', verbose_name='Video')),
                ('ppt', models.FileField(blank=True, upload_to='images/', verbose_name='Presentations')),
                ('Notes', models.FileField(blank=True, upload_to='images/', verbose_name='Notes')),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.lesson')),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.standard')),
            ],
        ),
    ]
