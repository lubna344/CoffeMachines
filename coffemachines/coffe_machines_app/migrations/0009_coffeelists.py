# Generated by Django 3.0.3 on 2020-09-16 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffe_machines_app', '0008_auto_20200916_0731'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeLists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lists', models.CharField(max_length=300)),
            ],
        ),
    ]
