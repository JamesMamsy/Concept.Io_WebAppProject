from django.contrib import admin

from conceptio.models import Project, Image, Category, Comment

admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Comment)


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


admin.site.register(Project, ProjectAdmin)
