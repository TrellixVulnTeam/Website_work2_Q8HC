# Generated by Django 3.1.4 on 2021-01-30 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0009_auto_20210130_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='comment',
            field=models.CharField(default='', max_length=1000),
        ),
    ]