# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

class CoffeeMachines(models.Model):
    product_type = models.CharField(max_length= 300)
    water_line_compitable = models.BooleanField()

    def __str__(self):
        return self.product_type


class CoffeePods(models.Model):
    product_types = models.CharField(max_length= 300)
    # pack_size = models.IntegerField()

    def __str__(self):
        return self.product_types

class CoffeeFlavors(models.Model):
    flavors = models.CharField(max_length=200)
    pack_sizes = models.CharField(max_length=100)

    def __str__(self):
        return self.flavors

class CoffeeLists(models.Model):
    types_choices = [
    ('Machines', (
            ('cm001', 'CM001'),
            ('cm002', 'CM002'),
            ('cm003', 'CM003'),
            ('cm101', 'CM101'),
            ('cm102', 'CM102'),
            ('cm103', "CM103")
        )
    ),
    ('Pods', (
            ('cp001', 'CP001'),
            ('cp002', 'CP002'),
            ('cp003', 'CP003'),
            ('cp011', 'CP011'),
            ('cp013', 'CP013'),
            ('cp021', 'CP021'),
            ('cp023', 'CP023'),
            ('cp031', 'CP031'),
            ('cp033', 'CP033'),
            ('cp041', 'CP041'),
            ('cp043', 'CP043'),
            ('cp101', 'CP101'),
            ('cp103', 'CP103'),
            ('cp111', 'CP111'),
            ('cp113', 'CP113'),
            ('cp121', 'CP121'),
            ('cp123', 'CP123'),
            ('cp131', 'CP131'),
            ('cp133', 'CP133'),
            ('cp141', 'CP141'),
            ('cp143', 'CP143')

        )
    ),
    ('Espresso', (
            ('em001', 'EM001'),
            ('em002', 'EM002'),
            ('em003', 'EM003'),
            ('ep003', 'EP003'),
            ('ep005', 'EP005'),
            ('ep007', "EP007"),
            ('ep013', "EP013"),
            ('ep015', "EP015"),
            ('ep017', "EP017"),
        )
    ),
]

    lists = models.CharField(max_length=300)
    types = models.CharField(max_length=100, choices = types_choices, default ='CM101')

    def __str__(self):
        return self.lists