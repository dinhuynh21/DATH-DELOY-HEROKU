# Generated by Django 3.0.6 on 2020-06-06 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200605_2328'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkinclass',
            options={'ordering': ['id_student'], 'verbose_name_plural': 'Thời khóa biểu cá nhân'},
        ),
    ]