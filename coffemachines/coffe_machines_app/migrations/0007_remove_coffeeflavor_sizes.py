# Generated by Django 3.0.3 on 2020-09-16 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffe_machines_app', '0006_auto_20200916_0722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffeeflavor',
            name='sizes',
        ),
    ]
