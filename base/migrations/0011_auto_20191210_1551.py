# Generated by Django 2.2.7 on 2019-12-10 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20191203_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='thighs',
        ),
        migrations.AddField(
            model_name='profile',
            name='bust',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='bust'),
        ),
        migrations.AddField(
            model_name='profile',
            name='height',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='height'),
        ),
    ]