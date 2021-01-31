from django.contrib import admin

from .models import Request, Item


# Register your models here.
class RequestList(admin.ModelAdmin):
    list_display = ('username', 'request_date', 'status')
    list_filter = ('username', 'request_date')
    ordering = ['username']


class ItemList(admin.ModelAdmin):
    list_display = ('item_name', 'item_quantity')
    list_filter = ('item_name','item_quantity')


admin.site.register(Request, RequestList)
admin.site.register(Item, ItemList)
