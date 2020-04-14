from django.contrib import admin
from main.models import Todo, MyUser


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_by', )
    search_fields = ('title', )
    ordering = ('-title', )


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', )
