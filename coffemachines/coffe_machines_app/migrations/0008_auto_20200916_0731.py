# Generated by Django 3.0.3 on 2020-09-16 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffe_machines_app', '0007_remove_coffeeflavor_sizes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CoffeeFlavor',
            new_name='CoffeeFlavors',
        ),
    ]
