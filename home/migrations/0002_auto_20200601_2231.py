# Generated by Django 3.0.6 on 2020-06-01 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classname',
            name='datecount',
            field=models.IntegerField(blank=True, default=0, verbose_name='Số buổi học'),
        ),
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayname', models.CharField(blank=True, max_length=50, null=True, verbose_name='Buổi')),
                ('note', models.CharField(blank=True, max_length=300, null=True, verbose_name='Ghi chú')),
                ('active', models.BooleanField(default=True, verbose_name='Trạng thái')),
                ('classname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Classname')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Room')),
            ],
        ),
        migrations.CreateModel(
            name='checkInClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayname', models.CharField(blank=True, max_length=50, null=True, verbose_name='Buổi')),
                ('note', models.CharField(blank=True, max_length=300, null=True, verbose_name='Ghi chú')),
                ('active', models.BooleanField(default=True, verbose_name='Trạng thái')),
                ('classname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Classname')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Room')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Student')),
            ],
        ),
    ]
