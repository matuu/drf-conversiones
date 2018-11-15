from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from core.models import Perfil, Registro


class ProfileInline(admin.StackedInline):
    model = Perfil
    max_num = 1
    min_num = 0
    fk_name = 'usuario'


class CustomUserAdmin(UserAdmin):
    inlines = UserAdmin.inlines + [ProfileInline]


class RegistroAdmin(admin.ModelAdmin):
    model = Registro


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Registro, RegistroAdmin)
