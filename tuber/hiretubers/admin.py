from django.contrib import admin
from .models import Hiretuber

# Register your models here.

class HiretuberAdmin(admin.ModelAdmin):
    
    def name(self, object):
        return ("%s %s" % (object.first_name, object.last_name))


    list_display = ('name', 'email', 'tuber_name')
    list_display_links = ('name',)
    search_fields =  ('first_name', 'last_name')
    list_filter = ('tuber_name', 'city', 'state')


admin.site.register(Hiretuber, HiretuberAdmin)
