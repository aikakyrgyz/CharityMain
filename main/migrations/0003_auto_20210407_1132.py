# Generated by Django 3.1 on 2021-04-07 05:32

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210407_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateField(default=datetime.datetime(2021, 4, 7, 5, 32, 45, 587912, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.article'),
        ),
    ]