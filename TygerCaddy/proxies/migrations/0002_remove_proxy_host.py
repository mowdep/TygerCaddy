# Generated by Django 2.0.3 on 2018-05-13 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proxies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proxy',
            name='host',
        ),
    ]
