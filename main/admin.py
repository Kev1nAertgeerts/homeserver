from django.contrib import admin
from . import models


class TabelAdmin(admin.ModelAdmin):
    list_display=("pot_nummer", "omschrijving", "personen", "datum")

# Register your models here.
admin.site.register(models.Diepvries, TabelAdmin)