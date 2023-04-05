from django.contrib import admin
from .models import Category, Product, SearchTerm, Order, OrderItem, Brand, Size

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Product)
admin.site.register(SearchTerm)
admin.site.register(Order)
admin.site.register(OrderItem)