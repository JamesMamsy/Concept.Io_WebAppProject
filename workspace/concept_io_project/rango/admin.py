from django.contrib import admin
from rango.models import Project,Image


admin.site.register(Image)

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
# Update the registration to include this customised interface
admin.site.register(Project,ProjectAdmin)