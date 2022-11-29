from django.contrib import admin
from .models import Contactinfo

# Register your models here.

class ContactinfoAdmin(admin.ModelAdmin):

    list_display = ('email', 'phone', 'created_date', 'edited_date')
    list_display_links = ('edited_date',)

admin.site.register(Contactinfo, ContactinfoAdmin)
