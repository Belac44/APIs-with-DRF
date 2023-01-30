from rest_framework import serializers
from .models import MenuItem, Order, OrderItem, Cart, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = MenuItem
        fields = ['title', 'price', 'featured', 'category', 'category_id']