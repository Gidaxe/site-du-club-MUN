from django.contrib import admin

from .models import *


class AccueilIntroMunAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(AccueilIntroMun, AccueilIntroMunAdmin)



