
from django.contrib import admin
from django.urls import path
from taskes.views import list_create_task, get_update_delete_task

urlpatterns = [
    path('admin/', admin.site.urls),

    path('tasks/', list_create_task, name='list_create_task'),

    path('tasks/<int:pk>', get_update_delete_task, name='get_update_delete_task'),
]
