# Generated by Django 3.1 on 2021-04-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_sign_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=250)),
                ('location', models.CharField(default='Bishkek/Kyrgyzstan', max_length=100)),
            ],
        ),
    ]
