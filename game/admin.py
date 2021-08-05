from django.contrib import admin
from .models import Inventory,Item,InventoryItem, Char, InventoryChar

admin.site.register(Inventory)
admin.site.register(Item)
admin.site.register(InventoryItem)
admin.site.register(Char)
admin.site.register(InventoryChar)
