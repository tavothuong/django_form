# Generated by Django 3.0.5 on 2020-05-02 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=1000)),
                ('time_create', models.DateTimeField(default=datetime.datetime(2020, 5, 2, 7, 18, 4, 709545))),
            ],
        ),
    ]