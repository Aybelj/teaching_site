# Generated by Django 3.1.1 on 2020-09-29 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0013_auto_20200929_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
