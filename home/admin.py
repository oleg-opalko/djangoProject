from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from home.models import MenuItem


# Register your models here.

@admin.register(MenuItem)
class MenuItemAdmin(MPTTModelAdmin):
    list_display = ['created_at','title', 'url','parent']
    list_editable = ('title', 'url', 'parent')
    search_fields = ('title',)