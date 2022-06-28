from django.contrib import admin

# Register your models here.
from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['description', 'status', 'done_at']
    list_display_links = ['description', 'status', 'done_at']
    list_filter = ['done_at']
    search_fields = ['done_at']
    fields = ['description', 'status', 'done_at']
    readonly_fields = []


admin.site.register(Task, TaskAdmin)