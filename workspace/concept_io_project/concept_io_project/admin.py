from django.contrib import admin
from concept_io_project.models import Page
from concept_io_project.models import UserProfile


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Page, PageAdmin)