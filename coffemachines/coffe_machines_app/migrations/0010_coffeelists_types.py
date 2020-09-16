# Generated by Django 3.0.3 on 2020-09-16 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffe_machines_app', '0009_coffeelists'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffeelists',
            name='types',
            field=models.CharField(choices=[('Machines', (('cm101', 'CM101'), ('cm102', 'CM102'), ('cm103', 'CM103'))), ('Pods', (('cp101', 'CP101'), ('cp103', 'CP103'), ('cp11', 'CP111'), ('cp113', 'CP113'), ('cp121', 'CP121'), ('cp123', 'CP123'), ('cp131', 'CP131'), ('cp141', 'CP141'), ('cp143', 'CP143'))), ('Espresso', (('ep003', 'EP003'), ('ep005', 'EP005'), ('ep007', 'EP007')))], default='CM101', max_length=100),
        ),
    ]
