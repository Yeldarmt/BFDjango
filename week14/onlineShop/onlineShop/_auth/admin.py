from django.contrib import admin
from onlineShop._auth.models import MyUser


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'password', 'is_staff', 'role')
