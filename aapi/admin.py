from django.contrib import admin

from aapi.models import Recebedor


@admin.register(Recebedor)
class RecebedorAdmin(admin.ModelAdmin):
    exclude = ()

