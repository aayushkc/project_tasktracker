from django.contrib import admin

from .models import Task
# Register your models here.
class AdminTask(admin.ModelAdmin):
    list_display = ('task_title', 'task_desc', 'task_category',\
        'task_assign_date', 'task_end_date')
    list_filter = ('task_title', 'task_assign_date')
    search_fields = ('task_title', 'task_assign_date')

admin.site.register(Task, AdminTask)

# customizing admin panel label
admin.site.site_header = "Task Tracker"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Task Tracker"
