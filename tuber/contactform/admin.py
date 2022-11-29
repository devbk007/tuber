from django.contrib import admin
from .models import Contactform

# Register your models here.

class ContactFormAdmin(admin.ModelAdmin):

    list_display = ('full_name', 'email', 'phone', 'subject')
    list_display_links = ('full_name',)
    search_fields =  ('subject',)

admin.site.register(Contactform, ContactFormAdmin)
