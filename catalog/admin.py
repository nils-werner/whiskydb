from django.contrib import admin
from models import Distillery, Variety, Whisky


class DistilleryAdmin(admin.ModelAdmin):
    pass


class VarietyAdmin(admin.ModelAdmin):
    pass


class WhiskyAdmin(admin.ModelAdmin):
    list_display = ('name', 'distillery', 'age', 'variety')


admin.site.register(Distillery, DistilleryAdmin)
admin.site.register(Variety, VarietyAdmin)
admin.site.register(Whisky, WhiskyAdmin)
