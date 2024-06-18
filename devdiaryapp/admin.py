from django.contrib import admin
from .models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("task", "due_date", "is_completed", "due_date", "created_at")
