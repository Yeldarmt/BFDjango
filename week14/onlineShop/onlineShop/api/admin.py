from django.contrib import admin
from onlineShop.api.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'count', 'category')