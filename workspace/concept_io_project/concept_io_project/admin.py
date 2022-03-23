from django.contrib import admin



class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Page, PageAdmin)