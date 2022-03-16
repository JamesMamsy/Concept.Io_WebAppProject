from django.contrib import admin

from rango.models import Project,Image
from rango.models import Page

admin.site.register(Image)

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Page, PageAdmin)
admin.site.register(Project,ProjectAdmin)
