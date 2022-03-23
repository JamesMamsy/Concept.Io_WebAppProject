from django.contrib import admin

<<<<<<< HEAD
from rango.models import Project,Image
from rango.models import Page

admin.site.register(Image)
=======
from conceptio.models import Project,Image, Category, Comment

admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Comment)
>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

<<<<<<< HEAD
admin.site.register(Page, PageAdmin)
admin.site.register(Project,ProjectAdmin)
=======
admin.site.register(Project,ProjectAdmin)

>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c
