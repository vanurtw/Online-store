from django.contrib import admin
from cart.models import Cart, Order


# Register your models here.

class StatusOrdeFilter(admin.SimpleListFilter):
    title = 'Фильтрация по статусу заказа'
    parameter_name = 'status_order'

    def lookups(self, request, model_admin):
        return [('DE', 'В доставке'),
                ('DR', 'Доставлен'),
                ('SR', 'Завершен')]

    def queryset(self, request, queryset):
        if self.value() == 'DE':
            return Order.objects.filter(status='DE')
        elif self.value() == 'DR':
            return Order.objects.filter(status='DR')
        elif self.value() == 'SR':
            return Order.objects.filter(status='SR')
        return Order.objects.all()


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'data_create']
    fields = ['user', 'product', 'quantitu', 'data_create']
    readonly_fields = ['data_create']
    search_fields = ['user__username']
    list_filter = ['data_create']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'data_create']
    readonly_fields = ['data_create']
    list_display_links = ['user', 'id']
    list_filter = ['data_create', StatusOrdeFilter]
    search_fields = ['first_name', 'last_name', 'user__username']
    actions = ['update_status']

    @admin.action(description='Поставить статус доставлен')
    def update_status(self, request, quereset):
        quereset.update(status='DR')
