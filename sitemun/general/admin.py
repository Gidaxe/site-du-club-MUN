from django.contrib import admin

from .models import *


class BackgroundAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class FooterAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class NavBarAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class GenerationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Background, BackgroundAdmin)

admin.site.register(Footer, FooterAdmin)

admin.site.register(NavBar, NavBarAdmin)

admin.site.register(Generation, GenerationAdmin)
