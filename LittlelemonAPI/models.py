from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField, DecimalField, SlugField, BooleanField, ForeignKey, SmallIntegerField, DateField


class Category(models.Model):
    slug = SlugField()
    title = CharField(max_length=255, db_index=True)

    def __str__(self) -> str:
        return f"{self.title}"

class MenuItem(models.Model):
    title = CharField(max_length=255, db_index=True)
    price = DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = BooleanField(db_index=True)
    category = ForeignKey(Category, on_delete=models.PROTECT, default=1)

    def __str__(self) -> str:
        return f"{self.title}"

class Cart(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)
    menuitem = ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = SmallIntegerField()
    unit_price = DecimalField(max_digits=6, decimal_places=2)
    price = DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('menuitem', 'user')


class Order(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = ForeignKey(User, on_delete=models.SET_NULL, related_name='delivery_crew', null=True)
    status = BooleanField(db_index=True, default=0)
    total = DecimalField(max_digits=6, decimal_places=2)
    date = DateField(db_index=True)

class OrderItem(models.Model):
    order = ForeignKey(User, on_delete=models.CASCADE)
    menuitem = ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = SmallIntegerField()
    unit_price = DecimalField(max_digits=6, decimal_places=2)
    price = DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('order', 'menuitem')
