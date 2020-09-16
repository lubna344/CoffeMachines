from rest_framework import serializers
from .models import CoffeeMachines, CoffeePods, CoffeeFlavors, CoffeeLists


class Coffee_MachinesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoffeeMachines
        fields = ['id', 'product_type', 'water_line_compitable']

        def create(self, validated_data):
            return CoffeeMachines.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
            instance.product_type = validated_data.get('product_type', instance.product_type)
            instance.water_line_compitable = validated_data.get('wate_line_compitable', instance.water_line_compitable)
            instance.save()
            return instance    

class Coffee_PodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoffeePods
        fields = ['id', 'product_types']

        def create(self, validated_data):
            return CoffeePods.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
            instance.product_types = validated_data.get('product_types', instance.product_types)
            instance.save()
            return instance

class Coffee_FlavorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoffeeFlavors
        fields = ['id', 'flavors', 'pack_sizes']

        def create(self, validated_data):
            return CoffeeFlavors.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
            instance.flavors = validated_data.get('flavors', instance.flavors)
            instance.pack_sizes= validated_data.get('pack_sizes', instance.pack_sizes)
            instance.save()
            return instance

class Coffee_ListsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoffeeLists
        fields = ['id', 'lists','types']

        def create(self, validated_data):
            return CoffeeLists.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
            instance.lists = validated_data.get('lists', instance.lists)
            instance.types = validated_data.get('types', instance.types)
            instance.save()
            return instance