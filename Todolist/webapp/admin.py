from django.contrib import admin

# Register your models here.
from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'done_at', 'name']
    list_display_links = ['name']
    list_filter = ['done_at']
    search_fields = ['done_at']
    fields = ['description', 'status', 'done_at', 'name']
    readonly_fields = []


admin.site.register(Task, TaskAdmin)
