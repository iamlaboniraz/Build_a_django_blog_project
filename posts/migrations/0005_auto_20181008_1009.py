# Generated by Django 2.1.1 on 2018-10-08 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20181008_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='draft',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='publish',
        ),
    ]
