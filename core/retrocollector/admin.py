from django.contrib import admin
from .models import Collectible, Type


class CollectibleAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'date_manufactured', 'date_added', 'description']


admin.site.register(Collectible, CollectibleAdmin)
admin.site.register(Type)

