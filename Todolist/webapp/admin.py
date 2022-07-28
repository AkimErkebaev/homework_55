from django.contrib import admin

# Register your models here.
from webapp.models import Task, Status, Type, Project


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'created_at', 'updated_at']
    list_display_links = ['name']
    list_filter = ['created_at']
    search_fields = ['created_at']
    fields = ['name', 'description', 'status', 'types']
    readonly_fields = []
    filter_horizontal = ['types']


admin.site.register(Task, TaskAdmin)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Project)
