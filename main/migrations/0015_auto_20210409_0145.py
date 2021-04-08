# Generated by Django 3.1 on 2021-04-08 19:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0014_auto_20210408_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateField(default=datetime.datetime(2021, 4, 8, 19, 45, 45, 223661, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='petitions')),
                ('created', models.DateField(default=datetime.datetime(2021, 4, 8, 19, 45, 45, 227626, tzinfo=utc))),
                ('goal_money', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('current_money', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('goal_signature', models.IntegerField()),
                ('current_signature', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='petitions', to='main.category')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='petitions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]