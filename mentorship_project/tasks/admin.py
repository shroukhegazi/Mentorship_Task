from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class Admin_Post (admin.ModelAdmin):
     list_display = ["id","title", "status"]