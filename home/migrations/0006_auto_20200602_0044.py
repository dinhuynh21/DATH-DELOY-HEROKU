# Generated by Django 3.0.6 on 2020-06-01 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200602_0037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkinclass',
            name='classname',
        ),
        migrations.RemoveField(
            model_name='checkinclass',
            name='room',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='room',
        ),
    ]