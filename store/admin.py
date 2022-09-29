from django.contrib import admin
from . models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date', 'affiliate_link')
    search_fields = ('name', 'price', 'date')
    list_filter = ('name', 'date', 'date')

    def __str__(self):
        return self.name
