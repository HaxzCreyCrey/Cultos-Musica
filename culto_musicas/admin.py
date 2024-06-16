from django.contrib import admin

from culto_musicas.models import Cultos

@admin.register(Cultos)
class CultosAdmin(admin.ModelAdmin):
    ...
