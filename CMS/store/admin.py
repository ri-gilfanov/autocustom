from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter
from .models import (
    Brand, Category, Product,
)


''' Бренды '''


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']


''' Категории '''


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    raw_id_fields = ['parent']
    search_fields = ['name']
    list_display = ['tree_actions', 'indented_title']
    prepopulated_fields = {'slug': ('name',)}


""" Товары """


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_filter = (
        ('category', TreeRelatedFieldListFilter),
        'brand',
    )
    raw_id_fields = ['brand', 'category']
    list_display = ['name', 'base_price']
    search_fields = ['name']
    list_per_page = 100
    prepopulated_fields = {'slug': ('name',)}
