from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Categories)
admin.site.register(Manufacturers)
admin.site.register(ImageProduct)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'category', 'sale', 'new_product']
    list_editable = ['price', 'category', 'sale', 'new_product']
    exclude = ['price']
    list_per_page = 10
    search_fields = ['product_name__contains']
    actions = ['update_new', 'update_no_new']

    @admin.action(description='Установить флаг новй товар')
    def update_new(self, request, quereset):
        quereset.update(new_product=True)

    @admin.action(description='Снять флаг с нового товара')
    def update_no_new(self, request, quereset):
        quereset.update(new_product=False)
