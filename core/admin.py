from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import FormAttention, FormPersonality, FormLearning


class FormAttentionAdmin(admin.ModelAdmin):
    list_display_links = ('user',)
    search_fields = ('user',)
    list_display = (
        "user",
        "questao1",
        "questao2",
        "questao3",
        "questao4",
        "questao5")


class FormPersonalityAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "questao1",
        "questao2",
        "questao3")


class FormLearningAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "questao1",
        "questao2",
        "questao3",
        "questao4",
        "questao5")


class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'codename')


admin.site.register(FormAttention, FormAttentionAdmin)
admin.site.register(FormPersonality, FormPersonalityAdmin)
admin.site.register(FormLearning, FormLearningAdmin)

admin.site.register(Permission, PermissionAdmin)
