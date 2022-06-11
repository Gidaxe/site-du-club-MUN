from django.contrib import admin

from .models import BigSlider, PresentationClub, Membre

from toolbox.forms import MemberForm


class PresentationClubAdmin(admin.ModelAdmin):
    list_display = ('titre', )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class MembreAdmin(admin.ModelAdmin):
    form = MemberForm


class BigSliderAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(PresentationClub, PresentationClubAdmin)

admin.site.register(Membre, MembreAdmin)

admin.site.register(BigSlider, BigSliderAdmin)


