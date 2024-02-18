from django.contrib import admin
from .models import DuvelCollection

# Register your models here.
class DuvelListview(admin.ModelAdmin):
    list_display = ("name", "year", "price")

admin.site.register(DuvelCollection, DuvelListview)