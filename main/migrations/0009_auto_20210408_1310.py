# Generated by Django 3.1 on 2021-04-08 07:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210408_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateField(default=datetime.datetime(2021, 4, 8, 7, 10, 35, 125352, tzinfo=utc)),
        ),
    ]