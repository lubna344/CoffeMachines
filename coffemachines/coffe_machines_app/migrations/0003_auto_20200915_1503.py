# Generated by Django 3.0.3 on 2020-09-15 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffe_machines_app', '0002_coffeeflavor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coffeepods',
            old_name='product_type2',
            new_name='product_types',
        ),
        migrations.DeleteModel(
            name='CoffeeFlavor',
        ),
    ]
