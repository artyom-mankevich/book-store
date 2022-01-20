from django.contrib import admin

# Register your models here.
from .models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    search_help_text = "You can search for user's username"

    fieldsets = [
        (None, {'fields': ['user', 'order_date', 'complete', 'total_price']}),
    ]
    inlines = [OrderItemInline]
    list_display = ('id', 'user', 'order_date', 'total_price')
    list_filter = ('order_date', 'total_price', 'complete')
    search_fields = ('user__username', )


class OrderItemAdmin(admin.ModelAdmin):
    @admin.display(description='Total price')
    def total_price(self, obj):
        return str(obj.quantity * obj.book.price)

    fields = ['quantity', 'order', 'book']
    list_display = ('id', 'book', 'quantity', 'total_price')
    list_filter = ('quantity', 'book__publisher__name', 'book__author__full_name')
    search_fields = ('book__isbn', 'book__title', )
    search_help_text = "You can look for book's isbn or title"


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)