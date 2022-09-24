from django.contrib import admin

from webapp.models import Picture, Album


# Register your models here.


class PictureAdmin(admin.ModelAdmin):
    list_display = ['caption']
    list_display_links = ['caption']
    list_filter = ['created_at']
    search_fields = ['caption', 'author', 'album']
    fields = ['picture', 'caption', 'author', 'album', 'private', 'favourites']
    readonly_fields = ['created_at']


admin.site.register(Picture, PictureAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    list_filter = ['created_at']
    search_fields = ['name', 'author']
    fields = ['name', 'description', 'author']
    readonly_fields = ['created_at']


admin.site.register(Album, AlbumAdmin)
