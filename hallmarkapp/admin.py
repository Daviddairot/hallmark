from django.contrib import admin
from .models import Item
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('bookname', 'item_image', 'term')
    list_filter = ('bookname', 'item_image', 'term')
    search_fields = ('bookname', 'item_image', 'term')