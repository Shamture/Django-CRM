# Generated by Django 2.0 on 2018-04-11 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20170926_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'ADMIN'), ('USER', 'USER')], default='ADMIN', max_length=50),
            preserve_default=False,
        ),
    ]