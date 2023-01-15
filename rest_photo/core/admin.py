from django.contrib import admin
from core.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('people', 'author', 'photo', 'location', 'description','date')
    list_display_links = ('aurhor',)
    search_fields = ('people', 'author', 'date')
    list_filter = ('people', 'author', 'date')


admin.site.register(Photo)
