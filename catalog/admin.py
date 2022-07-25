from django.contrib import admin

from catalog.models import Inventories, Features, Properties, VendorCodes


class VendorCodesInline(admin.TabularInline):
    model = VendorCodes
    extra = 2


class FeaturesInline(admin.TabularInline):
    model = Features
    extra = 3


class PropertiesInline(admin.TabularInline):
    model = Properties
    extra = 4


class InventoriesAdmin(admin.ModelAdmin):
    list_display = ('exchange_id', 'inventories_name')
    # fieldsets = [
    #     ('Request information', {'fields': ['path', 'request_method']}),
    #     ('Form data information', {'fields': ['form_data']}),
    # ]
    # readonly_fields = ('path', 'request_method', 'form_data')
    # list_filter = ['timestamp']
    # search_fields = ['path']
    inlines = [VendorCodesInline, FeaturesInline]


class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('exchange_id', 'feature_name', 'feature_value')


class PropertiesAdmin(admin.ModelAdmin):
    list_display = ('exchange_id', 'inventories', 'features', 'property_name')


admin.site.register(Inventories, InventoriesAdmin)
admin.site.register(Features, FeaturesAdmin)
admin.site.register(Properties, PropertiesAdmin)
