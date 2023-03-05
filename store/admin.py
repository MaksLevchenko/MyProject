from django.contrib import admin

from store.models import Category, Product, UserProductFavorite


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProductFavorite)
class UserProductFavoriteAdmin(admin.ModelAdmin):
    pass
