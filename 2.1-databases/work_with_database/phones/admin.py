from django.contrib import admin
from .models import Phone

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'image', 'release_date', 'lte_exists']
    prepopulated_fields = {"slug": ("name", )}
    list_filter = ['name', 'price', 'lte_exists']
    pass