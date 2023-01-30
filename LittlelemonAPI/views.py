from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import MenuItemsSerializer


@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == "GET":
        items = MenuItem.objects.select_related('category').all()
        serialized_items = MenuItemsSerializer(items, many=True)
        return Response(serialized_items.data, status.HTTP_200_OK)
    elif request.method == "POST":
        serialized_data = MenuItemsSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        return Response(serialized_data.data, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT','PATCH','DELETE'])
def single_menu_item(request, pk):
    if request.method == "GET":
        item = get_object_or_404(MenuItem, pk=pk)
        serialized_item = MenuItemsSerializer(item)
        return Response(serialized_item.data, status.HTTP_200_OK)
    
    elif request.method == "PUT":
        item = get_object_or_404(MenuItem, pk=pk)
        serialized_data = MenuItemsSerializer(item, data=request.data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        return Response(serialized_data.data, status.HTTP_201_CREATED)
    
    elif request.method == "PATCH":
        item = get_object_or_404(MenuItem, pk=pk)
        serialized_data = MenuItemsSerializer(item, data=request.data, partial=True)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        return Response(serialized_data.data, status.HTTP_201_CREATED)

    elif request.method == "DELETE":
        item = get_object_or_404(MenuItem, pk=pk)
        item.delete()
        return Response({"details": "Deleted Successfully"},status.HTTP_204_NO_CONTENT)

