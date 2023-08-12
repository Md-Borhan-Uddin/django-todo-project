from django.contrib import admin

from todo.models import TodoModel

# Register your models here.

@admin.register(TodoModel)
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ('id','todoTitle','created')
    list_filter = ('is_completed',)
    search_fields = ('is_completed', 'todoTitle')