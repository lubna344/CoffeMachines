# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import CoffeeMachines, CoffeePods, CoffeeFlavors, CoffeeLists

# Register your models here.

admin.site.register(CoffeeMachines)
admin.site.register(CoffeePods)
admin.site.register(CoffeeFlavors)
admin.site.register(CoffeeLists)

