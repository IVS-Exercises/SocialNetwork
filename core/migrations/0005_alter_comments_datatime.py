# Generated by Django 3.2.16 on 2022-11-16 18:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20221108_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='dataTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 17, 1, 18, 0, 877617)),
        ),
    ]
