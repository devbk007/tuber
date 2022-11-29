from django.contrib import admin
from django.utils.html import format_html
from .models import Youtuber

# Register your models here.

class YoutuberAdmin(admin.ModelAdmin):
    
    def name(self, object):
        return ("%s %s" % (object.first_name, object.last_name))

    def pic(self, object):
        return format_html('<img src="{}" width="40" height="40"/>'.format(object.photo.url))

    list_display = ('name', 'pic', 'category', 'subs_count', 'is_featured')
    list_display_links = ('name',)
    search_fields =  ('first_name', 'last_name')
    list_filter = ('category', 'camera', 'city', 'is_featured', 'crew')
    list_editable = ('is_featured',)


admin.site.register(Youtuber, YoutuberAdmin)