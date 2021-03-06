# Generated by Django 3.0.3 on 2020-09-16 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffe_machines_app', '0014_auto_20200916_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeelists',
            name='types',
            field=models.CharField(choices=[('Machines', (('cm001', 'CM001'), ('cm002', 'CM002'), ('cm003', 'CM003'), ('cm101', 'CM101'), ('cm102', 'CM102'), ('cm103', 'CM103'))), ('Pods', (('cp001', 'CP001'), ('cp002', 'CP002'), ('cp003', 'CP003'), ('cp101', 'CP101'), ('cp103', 'CP103'), ('cp011', 'CP011'), ('cp113', 'CP113'), ('cp121', 'CP121'), ('cp123', 'CP123'), ('cp131', 'CP131'), ('cp141', 'CP141'), ('cp143', 'CP143'))), ('Espresso', (('em001', 'EM001'), ('em002', 'EM002'), ('em003', 'EM003'), ('ep003', 'EP003'), ('ep005', 'EP005'), ('ep007', 'EP007'), ('ep013', 'EP013'), ('ep015', 'EP015'), ('ep017', 'EP017')))], default='CM101', max_length=100),
        ),
    ]
