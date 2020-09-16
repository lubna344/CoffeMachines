# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Coffee_MachinesSerializer, Coffee_PodsSerializer, Coffee_FlavorsSerializer, Coffee_ListsSerializer
from .models import CoffeeMachines, CoffeePods, CoffeeFlavors, CoffeeLists


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.

class CoffeeMachinesViewSet(viewsets.ModelViewSet):
    queryset = CoffeeMachines.objects.all().order_by('product_type')
    serializer_class = Coffee_MachinesSerializer

@csrf_exempt
def CoffeeMachines(request):
    
    if request.method == 'GET':
        coffee = CoffeeMachines.objects.all()
        serializer = Coffee_MachinesSerializer(CoffeeMachines, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Coffee_MachinesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def CoffeeMachines(request, pk):

    try:
        snippet = CoffeeMachines.objects.get(pk=pk)
    except CoffeeMachines.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Coffee_MachinesSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Coffee_MachinesSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

        #Coffe-Pods#

class CoffeePodsViewSet(viewsets.ModelViewSet):
    queryset = CoffeePods.objects.all().order_by('product_types')
    serializer_class = Coffee_PodsSerializer

@csrf_exempt
def CoffeePods(request):
    
    if request.method == 'GET':
        coffee = CoffeePods.objects.all()
        serializer = Coffee_PodsSerializer(CoffeePods, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Coffee_PodsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def CoffeePods(request, pk):

    try:
        snippet = CoffeePods.objects.get(pk=pk)
    except CoffeePods.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Coffee_PodsSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Coffee_PodsSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

    #Coffee-Flavors#

class CoffeeFlavorsViewSet(viewsets.ModelViewSet):
    queryset = CoffeeFlavors.objects.all().order_by('flavors', 'pack_sizes')
    serializer_class = Coffee_FlavorsSerializer

@csrf_exempt
def CoffeeFlavors(request):
    
    if request.method == 'GET':
        coffee = CoffeeFlavors.objects.all()
        serializer = Coffee_FlavorsSerializer(CoffeeFlavors, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Coffee_FlavorsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def CoffeeFlavors(request, pk):

    try:
        snippet = CoffeeFlavors.objects.get(pk=pk)
    except CoffeeFlavors.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Coffee_FlavorsSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Coffee_FlavorsSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
        
    #Coffee-Lists#

class CoffeeListsViewSet(viewsets.ModelViewSet):
    queryset = CoffeeLists.objects.all().order_by('lists','types')
    serializer_class = Coffee_ListsSerializer
    
@csrf_exempt
def CoffeeLists(request):
    
    if request.method == 'GET':
        coffee = CoffeeLists.objects.all()
        serializer = Coffee_ListsSerializer(CoffeeLists, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Coffee_ListsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def CoffeeLists(request, pk):

    try:
        snippet = CoffeeLists.objects.get(pk=pk)
    except CoffeeMachines.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Coffee_ListsSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Coffee_ListsSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)



    


