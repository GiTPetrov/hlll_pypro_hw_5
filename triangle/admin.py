from django.contrib import admin

from triangle.models import Logs


class LogsAdmin(admin.ModelAdmin):
    list_display = ('path', 'request_method', 'form_data', 'timestamp')
    fieldsets = [
        ('Request information', {'fields': ['path', 'request_method']}),
        ('Form data information', {'fields': ['form_data']}),
    ]
    readonly_fields = ('path', 'request_method', 'form_data')
    list_filter = ['timestamp']
    search_fields = ['path']


admin.site.register(Logs, LogsAdmin)
