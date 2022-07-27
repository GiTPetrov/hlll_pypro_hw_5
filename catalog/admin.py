from django.contrib import admin

from catalog.models import Group, GroupPath, Inventories, FeatureName, Features, Properties, PropertyName, PropertySet, VendorCodes


class GroupPathInline(admin.TabularInline):
    model = GroupPath
    extra = 1


class VendorCodesInline(admin.TabularInline):
    model = VendorCodes
    extra = 1


class FeaturesInline(admin.TabularInline):
    model = Features
    extra = 1


class PropertiesInline(admin.TabularInline):
    model = Properties
    extra = 1


class PropertySetInline(admin.TabularInline):
    model = PropertySet
    extra = 1


class GroupAdmin(admin.ModelAdmin):
    list_display = ('exchange_id', 'group_name', 'parent')


class GroupPathAdmin(admin.ModelAdmin):
    list_display = ('ancestor', 'descendant', 'path_length')


class InventoriesAdmin(admin.ModelAdmin):
    list_display = ('exchange_id', 'inventory_name', 'group')
    # fieldsets = [
    #     ('Request information', {'fields': ['path', 'request_method']}),
    #     ('Form data information', {'fields': ['form_data']}),
    # ]
    # readonly_fields = ('path', 'request_method', 'form_data')
    # list_filter = ['timestamp']
    # search_fields = ['path']
    # inlines = [VendorCodesInline, PropertySetInline, FeaturesInline]


class FeatureNameAdmin(admin.ModelAdmin):
    list_display = ('exchange_id', 'feature_name')


class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('name', 'feature_value')


class PropertiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'property_value')


class PropertyNameAdmin(admin.ModelAdmin):
    list_display = ('property_name',)


class PropertySetAdmin(admin.ModelAdmin):
    list_display = ('exchange_id', 'property_set_name')


class VendorCodesAdmin(admin.ModelAdmin):
    list_display = ('vendor_code_company', 'vendor_code_supplier')


admin.site.register(Group, GroupAdmin)
admin.site.register(GroupPath, GroupPathAdmin)
admin.site.register(Inventories, InventoriesAdmin)
admin.site.register(FeatureName, FeatureNameAdmin)
admin.site.register(Features, FeaturesAdmin)
admin.site.register(Properties, PropertiesAdmin)
admin.site.register(PropertyName, PropertyNameAdmin)
admin.site.register(PropertySet, PropertySetAdmin)
admin.site.register(VendorCodes, VendorCodesAdmin)
