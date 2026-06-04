from django.contrib import admin
from .models import Category, Product, ProductVariant


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'slug',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'category',
        'price',
        'is_active',
        'is_featured',
        'is_new',
    )

    list_filter = (
        'category',
        'is_active',
        'is_featured',
        'is_new',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):

    list_display = (
        'product',
        'size',
        'color',
        'stock',
    )

    list_filter = (
        'size',
        'color',
    )