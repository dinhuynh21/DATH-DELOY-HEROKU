# Generated by Django 3.0.6 on 2020-06-02 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_checkinclass_id_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkinclass',
            name='id_student',
        ),
    ]