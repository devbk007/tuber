from django.contrib import admin
from .models import Slider, Team, About, Services, Chooseus
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def pic(self, object):
        return format_html('<img src="{}" width="40" height="40"/>'.format(object.photo.url))

    def name(self, object):
        if object.gender.upper() == 'M':
            return ("%s %s" % ("Mr." + object.first_name, object.last_name))
        elif object.gender.upper() == 'F':
            return ("%s %s" % ("Ms." + object.first_name, object.last_name))
        else:
            return ("%s %s" % (object.first_name, object.last_name))

    list_display = ('pic','name', 'role', 'created_date', 'edited_date') # Displaying attributes in admin panel rather than just object name
    list_display_links = ('name',) # To make clickable attributes. By default, id will be made clickable
    search_fields = ('first_name', 'last_name', 'role') # To add search field
    list_filter = ('created_date','role') # To make a filter at right side of page
    ordering = ['-edited_date'] # To display entries in ascending oder of creation

class SliderAdmin(admin.ModelAdmin):
    def pic(self, object):
        return format_html('<img src="{}" width="40" height="40"/>'.format(object.photo.url))
    
    list_display = ('headline', 'pic', 'button_text')
    list_display_links = ('headline',)

class AboutAdmin(admin.ModelAdmin):
    def pic(self, object):
        return format_html('<img src="{}" width="40" height="40"/>'.format(object.photo.url))

    list_display = ('pic', 'title')
    list_display_links = ('title',)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'fees', 'yt_link', 'edited_date')
    list_display_links = ('service_type',)

class ChooseusAdmin(admin.ModelAdmin):
    list_display = ('happy_customers', 'happy_creators', 'completed_projects')
    list_display_links = ('completed_projects',)

admin.site.register(Slider, SliderAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Chooseus, ChooseusAdmin)