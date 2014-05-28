from django.contrib import admin
from models import Distillery, Variety, Whisky


class DistilleryAdmin(admin.ModelAdmin):
    pass


class VarietyAdmin(admin.ModelAdmin):
    pass


class WhiskyAdmin(admin.ModelAdmin):
    list_display = ('name', 'distillery', 'age', 'variety', 'get_purchases')

    def get_purchases(self, obj):
        return obj.purchase_set.count()
    get_purchases.short_description = 'Purchases'

admin.site.register(Distillery, DistilleryAdmin)
admin.site.register(Variety, VarietyAdmin)
admin.site.register(Whisky, WhiskyAdmin)
