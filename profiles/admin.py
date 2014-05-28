from django.contrib import admin
from models import User, Purchase


class UserAdmin(admin.ModelAdmin):
    pass


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'whisky', 'get_variety', 'price')

    def get_variety(self, obj):
        return obj.whisky.variety
    get_variety.short_description = 'Variety'

admin.site.register(User, UserAdmin)
admin.site.register(Purchase, PurchaseAdmin)
