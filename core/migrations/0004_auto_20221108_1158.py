# Generated by Django 3.2.16 on 2022-11-08 04:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20221106_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='dataTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 8, 11, 58, 49, 517278)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='Content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='Title',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
