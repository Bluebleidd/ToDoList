from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'board')
    
    def is_completed(self, obj):
        return obj.status == Task.DONE
    is_completed.boolean = True

admin.site.register(Task, TaskAdmin)
