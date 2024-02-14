from django.contrib import admin
from .models import Sec

# Register your models here.
class Sec_admin(admin.ModelAdmin):
    list_display = ("key", "sec", "crypto_gr_key")

admin.site.register(Sec, Sec_admin)
