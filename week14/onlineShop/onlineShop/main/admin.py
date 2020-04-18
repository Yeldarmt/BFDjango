from django.contrib import admin
from onlineShop.main.models import Category, CategoryFullInfo


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(CategoryFullInfo)
class CategoryFullInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'category_info')

