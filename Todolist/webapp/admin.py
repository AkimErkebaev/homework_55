from django.contrib import admin

# Register your models here.
from webapp.models import Task, Status, Type


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'status', 'created_at', 'updated_at']
    list_display_links = ['name']
    list_filter = ['created_at']
    search_fields = ['created_at']
    fields = ['name', 'description', 'status', 'types']
    readonly_fields = []


admin.site.register(Task, TaskAdmin)
admin.site.register(Status)
admin.site.register(Type)