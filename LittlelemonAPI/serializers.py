from rest_framework import serializers
from .models import MenuItem, Order, OrderItem, Cart, Category

class MenuItemsSerilaizer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ['title', 'price', 'featured', 'category']