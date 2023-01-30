from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import MenuItemsSerilaizer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemsSerilaizer

@api_view(['GET', 'POST'])
def menu(request):
    return Response({'message': "This is a success"}, status.HTTP_200_OK)