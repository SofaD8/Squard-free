from django.contrib import admin
from .models import About, Services, PortfolioCategory, Photo, Team, Contact
from django.utils.safestring import mark_safe


admin.site.register(Contact)


# Register your models here.
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'sort')
    list_editable = ('name', 'description','sort')
    search_fields = ('name',)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description','is_visible','sort')
    list_editable = ('name', 'description', 'is_visible','sort')
    list_filter = ('is_visible',)
    search_fields = ('name',)


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort', 'slug')
    list_editable = ('name', 'sort', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'sort')
    list_editable = ('sort',)
    list_filter = ('category',)
    search_fields = ('sort',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=50 height=50>')

    photo_src_tag.short_description = 'Photo'


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'id', 'name', 'description','sort')
    list_editable = ('name', 'description', 'sort')
    search_fields = ('name', 'description')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=50 height=50>')

    photo_src_tag.short_description = 'Team'


