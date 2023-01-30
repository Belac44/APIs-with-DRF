from django.contrib import admin
from .models import Order, OrderItem, MenuItem, Cart, Category

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(MenuItem)
admin.site.register(Cart)
admin.site.register(Category)
